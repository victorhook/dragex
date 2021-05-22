from collections import namedtuple
import math


from .settings import Settings

Grid = namedtuple('Grid', ['row', 'col'])


def get_grid(y: int, x: int) -> Grid:
    """ Returns the correct grid, given the x and y coordinates of the screen.
    """
    row = y // Settings.GRID_SIZE
    col = x // Settings.GRID_SIZE
    return Grid(row, col)


positions = {
    0: 'NW',
    1: 'N',
    2: 'NE',
    3: 'E',
    4: 'SE',
    5: 'S',
    6: 'SW',
    7: 'W',
}


class Orientation:
    NW = 0
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7


class Position:

    def __init__(self, x: int = 0, y: int = 0,
                 orientation: int = Orientation.N):
        self.x = x
        self.y = y
        self.orientation = orientation

    def rotate(self, orientation: int) -> None:
        self.orientation = orientation

    def distance_to(self, grid: Grid) -> float:
        x = grid.col
        y = grid.row
        return math.hypot(self.x - x, self.y - y)

    def get_grid(self):
        return Grid(round(self.y), round(self.x))

    def __repr__(self):
        return f'Ori: {self.orientation} - {positions[self.orientation]} Pos: {self.get_grid()}'


class WorldPosition(Position):
    pass


class RelativePosition(Position):
    pass
