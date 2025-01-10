from random import choice
from shotgun import ShotGun


class Human:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.health = 4
        self.memory: dict[str, int] = {}
        self.pockets: list[tuple[str, str]] = []
        self.handcuffed = False

    def self_shot(self, shotgun: ShotGun):
        power = shotgun.shot()
        if power == 0:
            print("Повезло. Это был холостой патрон!")
            print(
                "-" * 50,
            )
        if power == 1:
            print("")
        if power:
            self.get_damage(power)
        return power

    def enemy_shot(self, shotgun: ShotGun, enemy):
        power = shotgun.shot()
        if power is not None:
            if power == 0:
                print("Это был холостой патрон.")
                print(
                    "-" * 50 + "\n",
                )
            enemy.get_damage(power)
            return power

    def get_damage(self, power: int):
        if self.health <= power:
            self.alive = False
        self.health -= power

    def get_random_items(self):

        items = [("1", "🍺"), ("2", "🔍"), ("3", "🚬"), ("4", "🔪"), ("5", "⛓")]
        while len(self.pockets) < 4:
            self.pockets.append(choice(items))

    def smoke_cigarette(self):
        if ('3', "🚬") in self.pockets:
            self.pockets.remove(("3", "🚬"))
            print(f"{self.name} выкурил сигарету. Восстановлена 1 жизнь.")
            if self.health < 4:
                self.health += 1

    def use_hand_saw(self, shotgun: ShotGun):
        if ('4', "🔪") in self.pockets:
            self.pockets.remove(("4", "🔪"))
            print("Была использована ручная пила. Дробовик имеет двойной урон!")
            shotgun.double_damage = True

    def use_magnifying_glass(self, shotgun: ShotGun):
        if ('2', "🔍") in self.pockets:
            self.pockets.remove(("2", "🔍"))
            print("Была использована лупа...")
        if shotgun.magazine:

            current = shotgun.magazine[-1]
            print("Следующий патрон на очереди - " + ["холостой.", "боевой."][current])
            return current

    def drink_beer(self, shotgun: ShotGun):
        if ('1', "🍺") in self.pockets:
            self.pockets.remove(("1", "🍺"))
            if shotgun.magazine:
                cartridge = shotgun.magazine.pop()
                print(["Холостой ", "Боевой "][cartridge] + "патрон пропущен.")

    def handcuff_opponent(self, enemy):
        if ('5', "⛓") in self.pockets:
            self.pockets.remove(("5", "⛓"))
            print(
                f"{self.name} одел наручники на {enemy.name} - он пропустит следующий ход."
            )
            enemy.handcuffed = True
