from utils import Settings
from .base_object import BaseObject


class GridMap:

    def __init__(self):
        self.length = Settings.GRID_AMMOUNT
        self.map = [[0 for i in range(self.length)]
                    for i in range(self.length)]

    def fill(self, game_objects: list) -> None:
        for row in range(self.length):
            for col in range(self.length):
                self[row, col] = 0

        for obj in game_objects:
            x, y = obj.position.x, obj.position.y
            self[y, x] = obj

    def __getitem__(self, pos: tuple) -> BaseObject:
        if type(pos) is int:
            return self.map[pos]
        else:
            row, col = pos
            return self.map[row][col]

    def __setitem__(self, pos: tuple, value: BaseObject) -> None:
        if type(pos) is int:
            self.map[pos] = value
        else:
            row, col = pos
            self.map[row][col] = value

    def __len__(self):
        return len(self.map)

    def __repr__(self):
        return str(self.map)
