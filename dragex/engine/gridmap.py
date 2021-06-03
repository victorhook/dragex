from utils import Settings, Singleton, Grid
from .base_object import BaseObject

from typing import List


class GridMap(Singleton):

    def init(self):
        self.length = Settings.GRID_AMMOUNT
        self.map = [[0 for i in range(self.length)]
                    for i in range(self.length)]

    def fill(self, game_objects: List[BaseObject]) -> None:
        for row in range(self.length):
            for col in range(self.length):
                self[row, col] = 0

        for obj in game_objects:
            for grid in obj.get_grids():
                self[grid.row, grid.col] = obj

    def is_empty(self, grid: Grid) -> bool:
        return self[grid.row, grid.col] == 0

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
