from random import choice
from time import sleep
from .human import Human
from shotgun import ShotGun


class Dealer(Human):
    def __init__(self, name):
        super().__init__(name)
        self.memory: dict[str, int] = {}

    def get_information(self, blank_сartridges, live_cartridges, enemy_health=4):
        self.memory = {
            "enemy_health": enemy_health,
            "blank_cartridges": blank_сartridges,
            "live_cartridges": live_cartridges,
        }

    def next_move(self):
        sleep(3)

        if self.pockets:
            print("Дилер выбирает предмет.")
            num, _ = choice(self.pockets)
            return num

        if self.memory["blank_cartridges"] >= 1 and self.memory["live_cartridges"] == 0:
            return "a"

        elif (
            self.memory["blank_cartridges"] == 0 and self.memory["live_cartridges"] >= 1
        ):
            solution = "b"
        else:
            solution = choice(["a", "b"])

        if solution == "a":
            print("Дилер решил стрелять в себя.")
        elif solution == "b":
            print("Дилер решил стрелять в вас.")
        sleep(4)
        return solution
