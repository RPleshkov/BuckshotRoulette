from random import choice, randint
from time import sleep
from .human import Human
from shotgun import ShotGun


class Dealer(Human):
    def __init__(self, name):
        super().__init__(name)
        self.memory: dict = {}

    def get_information(self, blank_сartridges, live_cartridges, enemy_health=4):
        self.memory = {
            "enemy_health": enemy_health,
            "blank_cartridges": blank_сartridges,
            "live_cartridges": live_cartridges,
            "current_cartridge": None,
            "used_items": set(),
        }

    def next_move(self):
        sleep(3)
        print(self.memory)
        solution = None

        if not solution and self.health < 4 and ("3", "🚬") in self.pockets:
            if self.health == 1 or choice([True, False]):
                solution = "3"

        if not solution and ("4", "🔪") in self.memory["used_items"]:
            solution = "b"

        if (
            not solution
            and self.memory["blank_cartridges"] >= 1
            and self.memory["live_cartridges"] == 0
            or self.memory["current_cartridge"] == 0
        ):
            solution = "a"

        if (
            not solution
            and self.memory["blank_cartridges"] == 0
            and self.memory["live_cartridges"] >= 1
            or self.memory["current_cartridge"] == 1
        ):
            if ("4", "🔪") in self.pockets and ("5", "⛓") not in self.memory[
                "used_items"
            ]:
                solution = "4"
                self.memory["used_items"].add(("4", "🔪"))
            if ("5", "⛓") in self.pockets and ("5", "⛓") not in self.memory[
                "used_items"
            ]:
                solution = "5"
                self.memory["used_items"].add(("5", "⛓"))

        if (
            not solution
            and self.memory["blank_cartridges"] > 0
            and self.memory["blank_cartridges"] > 0
        ):
            if ("2", "🔍") in self.pockets and ("2", "🔍") not in self.memory[
                "used_items"
            ]:
                solution = "2"
            if ("1", "🍺") in self.pockets and self.memory["current_cartridge"] != 0:
                solution = "1"

        if not solution and self.pockets:
            if randint(0, 1):
                item = choice(self.pockets)
                if item not in self.memory["used_items"]:
                    self.memory["used_items"].add(item)
                    solution = item[0]

        if not solution:
            solution = choice(["a", "b"])

        if solution == "a":
            print("Дилер решил стрелять в себя.")
        elif solution == "b":
            print("Дилер решил стрелять в вас.")
        else:
            print("Дилер выбирает предмет.")
        sleep(4)
        return solution
