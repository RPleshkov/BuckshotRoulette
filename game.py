from itertools import cycle
from random import randint
from time import sleep
from players import *
from shotgun import ShotGun
import shotgun


class BuckshotRoulette:
    def __init__(self):
        self.status_game = False
        self.current_round = 1

    def init_game(self):
        self.status_game = True
        print("Добро пожаловать в BuckshotRoulette!\n")
        name = input("Перед тем как начать, сообщи как тебя зовут: ")
        print("Игра началась!\n")
        self.dealer = Dealer("дилер")
        self.player = Player(name=name)
        self.shotgun = ShotGun()

    @staticmethod
    def generate_cartridges() -> list:
        cartridges = [1, 0]
        for _ in range(randint(0, 6)):
            cartridges.append(randint(0, 1))
        return cartridges

    @staticmethod
    def check_cartridges(cartridges: list) -> dict[str, int]:
        live = cartridges.count(1)
        blank = cartridges.count(0)
        return {"blank_сartridges": blank, "live_cartridges": live}

    @staticmethod
    def check_player_items(player: Player | Dealer, add_keys=False) -> str:
        if not add_keys:
            items = [pare[1] for pare in player.pockets]
            return "|".join(items)
        res = set()
        for num, item in player.pockets:
            res.add(f"{item} - {num}")
        return f'{"\n".join(res)}\nВвод: '

    def display_health(self):
        print(f"Здоровье дилера: {self.dealer.health * '❤'}")
        print(f"Твоё здоровье: {self.player.health * '❤'}\n")

    def display_items(self):
        print(f"Предметы дилера: {self.check_player_items(self.dealer)}")
        print(f"Твои предметы: {self.check_player_items(self.player)}\n")

    def engage_target(self, player: Player | Dealer, shotgun: ShotGun):
        print(f"Следующий ходит {player.name}")
        sleep(1)

        while True:
            if type(player) is Player:
                player_choice = input(
                    f"(a) - Выстрелить в себя / (b) - Выстрелить в дилера.\nВыбрать предмет:\n{self.check_player_items(player, add_keys=True)}"
                )
                enemy = self.dealer
            if type(player) is Dealer:
                player_choice = player.next_move()
                enemy = self.player

            if player_choice in "12345":

                match player_choice:
                    case "1":
                        player.drink_beer(shotgun=shotgun)
                    case "2":
                        player.use_magnifying_glass(shotgun=shotgun)
                    case "3":
                        player.smoke_cigarette()
                    case "4":
                        player.use_hand_saw(shotgun=shotgun)
                    case "5":
                        player.handcuff_opponent(enemy=enemy)
            else:
                break

        if player_choice == "a":
            result = player.self_shot(shotgun=self.shotgun)
        if player_choice == "b":
            result = player.enemy_shot(shotgun=self.shotgun, enemy=enemy)

        if result == 0:
            self.dealer.memory["blank_cartridges"] -= 1
            print(self.dealer.memory)
        else:
            self.dealer.memory["live_cartridges"] -= 1
            self.display_health()

        self.dealer.memory["enemy_health"] = self.player.health
        return result, player_choice

    def manage_queue(self):
        yield from cycle([self.player, self.dealer])

    def play(self):

        self.init_game()

        while self.status_game is True:

            print(f"{self.current_round} РАУНД.\n")

            cartridges = self.generate_cartridges()
            live_and_blank = self.check_cartridges(cartridges)
            print(
                "{live_cartridges} боевых. {blank_сartridges} холостых\n".format(
                    **live_and_blank
                )
            )

            self.display_health()
            self.dealer.get_information(**live_and_blank)
            print("Заряжаю обойму в случайной последовательности...\n")
            self.shotgun.charge(cartridges)
            sleep(4)
            print("Выдаем предметы...")
            sleep(3)

            self.player.get_random_items()
            self.dealer.get_random_items()
            self.display_items()

            if self.current_round == 1:
                print("Позволяю первый ход сделать тебе")

                queue = self.manage_queue()
                player = next(queue)

            while True:

                result, target = self.engage_target(player=player, shotgun=self.shotgun)
                if result == 0 and target == "a":
                    sleep(3)
                    if self.shotgun.magazine:
                        print("Так как игрок стрелял в себя, ход остается за ним.")
                        continue

                elif result == 1 or (result == 0 and target == "b"):
                    player = next(queue)

                if not (self.player.alive and self.dealer.alive):
                    text = ["Победил дилер.", "Поздравляю, ты победил!"]
                    print(text[self.player.alive])
                    self.status_game = False
                    break

                if not self.shotgun.magazine:
                    print("Патроны закончились.\n")
                    self.current_round += 1
                    break


game = BuckshotRoulette()
game.play()
