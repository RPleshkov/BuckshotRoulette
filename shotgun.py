import random


class ShotGun:
    def __init__(self):
        self.damage = 1
        self.double_damage = False
        self.magazine = []

    def charge(self, cartridges: list):
        self.magazine = cartridges.copy()
        random.shuffle(self.magazine)

    def shot(self):
        if self.double_damage:
            self.damage *= 2
        if self.magazine:
            result = self.magazine.pop()
            if result != 0:
                print("Прозвучал оглушительный выстрел. Это был боевой патрон.")
                print(
                    "-" * 50,
                )
            power = self.damage if result else 0
            self.damage = 1
            self.double_damage = False
            return power


