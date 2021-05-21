from collections import namedtuple
from .settings import Settings


class Position:

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __init__(self, x: int = 0, y: int = 0, orienation: int = NORTH):
        self.x = x
        self.y = y
        self.orienation = orienation

    def get_grid(self):
        return (self.x, self.y)


class WorldPosition(Position):
    pass


class RelativePosition(Position):
    pass


Grid = namedtuple('Grid', ['row', 'col'])


def get_grid(y: int, x: int) -> Grid:
    """ Returns the correct grid, given the x and y coordinates of the screen.
    """
    row = y // Settings.GRID_SIZE
    col = x // Settings.GRID_SIZE
    return Grid(row, col)
