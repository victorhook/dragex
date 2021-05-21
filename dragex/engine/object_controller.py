from collections import namedtuple
from utils import Position, Grid, Settings

from .pathfinder import PathFinder, Path
from .gridmap import GridMap


Vec2 = namedtuple('Vec2', ['x', 'y'])
STEPS_PER_GRID_SQUARE = 10
STEP_SIZE = Settings.GRID_SIZE / STEPS_PER_GRID_SQUARE


class ObjectController:

    dirs = {
        Position.NORTH: Vec2(0, 1),
        Position.EAST: Vec2(1, 0),
        Position.SOUTH: Vec2(0, -1),
        Position.WEST: Vec2(-1, 0)
    }

    def __init__(self, pos: Position):
        self.pos = pos
        self.vel = Vec2(0, 0)
        self.target = self.pos
        self.path_finder = PathFinder()
        self.curr_path = None
        self.next_grid = None

        self._tmp_pos = Vec2(pos.x, pos.y)
        self._step = 0

    def jump_to(self, x: int, y: int) -> None:
        self.pos.x = x
        self.pos.y = y

    def move(self) -> None:
        if self.curr_path is None or self.curr_path.arrived():
            return

        if self._step > STEPS_PER_GRID_SQUARE:
            self._step = 0
            self.next_grid = self.curr_path.next()
            self.set_direction()

        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

        self._step += 1

    def set_direction(self) -> None:
        dr = self.next_grid.row - self.pos.x
        dc = self.next_grid.col - self.pos.c

        if dr == 0 and dc == -1:
            self.pos.orienation = Position.WEST
        if dr == 0 and dc == 1:
            self.pos.orienation = Position.EAST
        if dr == 1 and dc == 0:
            self.pos.orienation = Position.NORTH
        if dr == -1 and dc == 0:
            self.pos.orienation = Position.SOUTH

        self.vel = self.dirs[self.pos.orienation]

    def set_target(self, target: Grid) -> None:
        self.target = None
        path = self.path_finder.find(GridMap(), self.pos.get_grid(), target)

        if path is not None:
            self.curr_path = path
            self.next_grid = self.curr_path.next()
