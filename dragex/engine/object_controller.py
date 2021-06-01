from collections import namedtuple
from utils import Position, Grid, Settings, Orientation

from engine.pathfinder import PathFinder, Path
from engine.gridmap import GridMap
from engine.object_state import ObjectState


Vec2 = namedtuple('Vec2', ['x', 'y'])
STEPS_PER_GRID_SQUARE = 10
STEP_SIZE = Settings.GRID_SIZE / STEPS_PER_GRID_SQUARE
ARRIVE_LIMIT = 0.5


"""
    Moving 1 square takes 5 ticks.
"""


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

    def __init__(self, pos: Position, state: ObjectState, speed: int = 10):
        self.pos = pos
        self.state = state
        self.speed = speed

        self.vel = Vec2(0, 0)
        self.path_finder = PathFinder()
        self.target = self.pos
        self.curr_path = None
        self.next_grid = None
        self.enemy_target = None

        self.dist = None
        self.closing_target = True
        self.interpolating = False

        self._tmp_pos = Vec2(pos.x, pos.y)
        self._step = 0

    def jump_to(self, grid: Grid) -> None:
        """ Sets the object to the given grid. """
        self.pos.x = grid.col
        self.pos.y = grid.row

    def move(self, elapsed_time: float) -> None:
        """
            Moves the object 1 interpolation.

            The position of an object is in forms of [y, x] or [row, col]
            of a grid matrix.
            This means each coordinate is discrete positions, aka integers.

            To move between two different grids, the object interpolates, so
            the y and x values are incremented by a size defined in the top
            of the file.

            This means that during movement, y and x positions are floating
            values, and to ensure that the object get to the correct grids
            and not overshooting, when the object is very close to being
            positioned entirely within a grid, jump_to() is invoked,
            to ensure concrete positions, inside each grid.
        """

        if self.curr_path is None:
            return

        if self.arrived():
            # We've arrive at the destination. Set concrete y, x positions.
            self.jump_to(self.curr_path.dst)
            self.curr_path = None
            self.next_grid = None

            # If arrived and we're chasing an enemy, we change to attack state.
            if self.enemy_target is not None:
                self.state.set(ObjectState.ATTACKING)
            else:
                self.state.set(ObjectState.IDLE)

            return

        elif not self.interpolating and self._within_next_grid():
            # We're within a grid, so we start interpolation, which means
            # we will not update directions until we're within the grid.
            self.interpolating = True
            self.dist = self.pos.distance_to(self.next_grid)

        elif self._hit_next_grid():
            # We're very close to the grid, jump to concrete y and x position.
            self.jump_to(self.next_grid)
            self.interpolating = False
            self.next_grid = self.curr_path.next()

        if not self.interpolating:
            self._update_directions()
        else:
            dist = self.pos.distance_to(self.next_grid)
            if dist > self.dist:
                self._update_directions()
                self.dist = dist

        # Update the positions.
        self.pos.x += self.vel.x * self.speed * elapsed_time
        self.pos.y += self.vel.y * self.speed * elapsed_time

    def arrived(self) -> bool:
        return self.pos.distance_to(self.curr_path.dst) < ARRIVE_LIMIT

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

    def attack_enemy(self, target: Grid, enemy) -> None:
        src = self.pos.get_grid()
        path = self.path_finder.attackable_path(GridMap(), src, target)
        self._set_path(path)
        self.enemy_target = enemy

    def set_target(self, target: Grid) -> None:
        self.target = None
        path = self.path_finder.find(GridMap(), self.pos.get_grid(), target)
        self.enemy_target = None
        self._set_path(path)

    def _set_path(self, path: Path) -> None:
        if path is not None:
            self.state.set(ObjectState.MOVING)
            self.curr_path = path
            self.next_grid = self.curr_path.next()
            self._update_directions()

    def _update_directions(self) -> None:
        self.set_direction()
        self.set_velocity()
        self.dist = self.pos.distance_to(self.next_grid)

    def _hit_next_grid(self) -> bool:
        return self.pos.distance_to(self.next_grid) < ARRIVE_LIMIT

    def _within_next_grid(self) -> bool:
        return self.pos.get_grid() == self.next_grid
