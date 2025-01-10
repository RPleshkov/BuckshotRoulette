from shotgun import ShotGun


class Human:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.health = 4
        self.memory: dict[str, int] = {}

    def self_shot(self, shotgun: ShotGun):
        power = shotgun.shot()
        if power == 0:
            print("Повезло. Это был холостой патрон!")
            print(
                "-" * 50,
            )
        if power == 1:
            print('')    
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
