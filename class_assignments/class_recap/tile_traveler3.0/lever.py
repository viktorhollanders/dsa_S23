import random


class Lever:
    def __init__(self, coins, position) -> None:
        self.coins = coins
        self.position = position
        self.pulled = False

    def initialize_levers(self):
        levers = set()
        while len(levers) < 4:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            if (x, y) not in [(1, 1), (3, 1)]:
                levers.add((x, y))
        return levers

    def pull_lever(self):
        print("You see a lever.")
        if input("PULL LEVER? (y/n): ").lower() == "y":
            self.coins += 1
            print("You received a gold coin!")
        return self.coins

    def has_lever(self, position):
        return position in [(1, 2), (2, 2), (2, 3), (3, 3)]
