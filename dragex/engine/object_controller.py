from collections import namedtuple
from utils import Position, Grid, Settings, Orientation

from .pathfinder import PathFinder, Path
from .gridmap import GridMap


Vec2 = namedtuple('Vec2', ['x', 'y'])
STEPS_PER_GRID_SQUARE = 40
STEP_SIZE = Settings.GRID_SIZE / STEPS_PER_GRID_SQUARE
ARRIVE_LIMIT = 0.5


class ObjectController:

    dirs = {
        Orientation.N: Vec2(0, -1),
        Orientation.NE: Vec2(1, -1),
        Orientation.E: Vec2(1, 0),
        Orientation.SE: Vec2(1, 1),
        Orientation.S: Vec2(0, 1),
        Orientation.SW: Vec2(-1, 1),
        Orientation.W: Vec2(-1, 0),
        Orientation.NW: Vec2(-1, -1)
    }

    def __init__(self, pos: Position, speed: int = 10):
        self.pos = pos
        self.vel = Vec2(0, 0)
        self.speed = speed
        self.path_finder = PathFinder()
        self.target = self.pos
        self.curr_path = None
        self.next_grid = None

        self.dist = None
        self.closing_target = True
        self.interpolating = False

        self._tmp_pos = Vec2(pos.x, pos.y)
        self._step = 0

    def jump_to(self, grid: Grid) -> None:
        self.pos.x = grid.col
        self.pos.y = grid.row

    def move(self, elapsed_time: float) -> None:
        if self.curr_path is None:
            return

        if self.arrived():
            self.jump_to(self.curr_path.dst)
            return
        elif not self.interpolating and self._within_next_grid():
            self.interpolating = True
            self.dist = self.pos.distance_to(self.next_grid)
        elif self._hit_next_grid():
            self.jump_to(self.next_grid)
            self.interpolating = False
            self.next_grid = self.curr_path.next()

        if not self.interpolating:
            self._update_directions()

        self.pos.x += self.vel.x * self.speed * elapsed_time
        self.pos.y += self.vel.y * self.speed * elapsed_time

    def _update_directions(self) -> None:
        self.set_direction()
        self.set_velocity()
        self.dist = self.pos.distance_to(self.next_grid)

    def is_close_to_arrival(self) -> bool:
        return self.pos.get_grid() == self.curr_path.dst

    def arrived(self) -> bool:
        return self.pos.distance_to(self.curr_path.dst) < ARRIVE_LIMIT

    def _hit_next_grid(self) -> bool:
        return self.pos.distance_to(self.next_grid) < ARRIVE_LIMIT

    def _within_next_grid(self) -> bool:
        return self.pos.get_grid() == self.next_grid

    def set_velocity(self) -> None:
        self.vel = self.dirs[self.pos.orientation]

    def set_direction(self) -> None:
        pos = self.pos.get_grid()
        dr = self.next_grid.row - pos.row
        dc = self.next_grid.col - pos.col

        if dr < 0 and dc == 0:
            self.pos.rotate(Orientation.N)
        elif dr < 0 and dc > 0:
            self.pos.rotate(Orientation.NE)

        elif dr == 0 and dc > 0:
            self.pos.rotate(Orientation.E)
        elif dr > 0 and dc > 0:
            self.pos.rotate(Orientation.SE)

        elif dr > 0 and dc == 0:
            self.pos.rotate(Orientation.S)
        elif dr > 0 and dc < 0:
            self.pos.rotate(Orientation.SW)

        elif dr == 0 and dc < 0:
            self.pos.rotate(Orientation.W)
        if dr < 0 and dc < 0:
            self.pos.rotate(Orientation.NW)

    def set_target(self, target: Grid) -> None:
        self.target = None
        path = self.path_finder.find(GridMap(), self.pos.get_grid(), target)

        if path is not None:
            self.curr_path = path
            self.next_grid = self.curr_path.next()
            self._update_directions()
