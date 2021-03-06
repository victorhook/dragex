from objects import BaseObject
from interfaces.screen import Screen
from objects import ObjectController
from objects import ControllableGameObject

from objects import Player


class Character(Player):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self, screen: Screen) -> None:
        super().draw(screen)
        return
        if self.ctrl.next_grid:
            from utils import Settings
            y0 = self.ctrl.next_grid.row * Settings.GRID_SIZE
            x0 = self.ctrl.next_grid.col * Settings.GRID_SIZE
            screen.create_rectangle(x0, y0, x0+Settings.GRID_SIZE,
                                    y0+Settings.GRID_SIZE, fill='red',
                                    tag='path')

    def update(self, elapsed_time: float) -> None:
        self.ctrl.move(elapsed_time)
