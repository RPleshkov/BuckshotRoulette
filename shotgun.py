import random


class ShotGun:
    def __init__(self):
        self.damage = 1
        self.magazine = []

    def charge(self, cartridges: list):
        self.magazine = cartridges.copy()
        random.shuffle(self.magazine)

    def shot(self):
        if self.magazine:
            result = self.magazine.pop()
            if result == 1:
                print("Прозвучал оглушительный выстрел. Это был боевой патрон.")
                print(
                    "-" * 50,
                )
            return result
