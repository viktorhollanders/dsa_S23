class Move:
    def __init__(self, walls, direction, position):
        self.walls = walls
        self.direction = direction
        self.position = position

    def move_player(self):
        if self.direction == "n":
            return (self.position[0], self.position[1] + 1)
        if self.direction == "s":
            return (self.position[0], self.position[1] - 1)
        if self.direction == "e":
            return (self.position[0] + 1, self.position[1])
        if self.direction == "w":
            return (self.position[0] - 1, self.position[1])
        return self.position

    def is_valid_move(self):
        if self.direction in self.walls.get(self.position, []):
            return False
        x, y = self.position

        if self.direction == "n" and y < 3:
            return True
        if self.direction == "s" and y > 1:
            return True
        if self.direction == "e" and x < 3:
            return True
        if self.direction == "w" and x > 1:
            return True
        return False
