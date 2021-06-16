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


class Orientation:
    NW = 0
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7


positions = {
    Orientation.NW: 'NW',
    Orientation.N: 'N',
    Orientation.NE: 'NE',
    Orientation.E: 'E',
    Orientation.SE: 'SE',
    Orientation.S: 'S',
    Orientation.SW: 'SW',
    Orientation.W: 'W',
}

rotations = {
    Orientation.NW: -135,
    Orientation.N: 180,
    Orientation.NE: 135,
    Orientation.E: 90,
    Orientation.SE: 45,
    Orientation.S: 0,
    Orientation.SW: -45,
    Orientation.W: -90,
}


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

    def get_rotation_angle(self) -> int:
        return rotations[self.orientation]

    def get_grid(self):
        return Grid(round(self.y), round(self.x))

    def __repr__(self):
        return f'Ori: {self.orientation} - {positions[self.orientation]} Pos: {self.get_grid()}'
