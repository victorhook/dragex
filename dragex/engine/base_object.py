from typing import List
import tkinter as tk
from tkinter.constants import ACTIVE

import utils
from engine.sprite import Sprite, SingleSprite
from engine.drawable import Drawable
from engine.interact import ExamineResponse, Action


def _get_default_size() -> utils.Size:
    return utils.Size(1, 1)


class BaseObject(Drawable):

    _obj_id = 0

    def __init__(self,
                 name: str = None,
                 desription: str = None,
                 world_x: int = 0,
                 world_y: int = 0,
                 orientation: int = 0,
                 visible: bool = True,
                 size: utils.Size = None,
                 active_sprite: Sprite = None,
                 ):
        self.name = _get_name(name)
        self.desription = desription
        self.position = utils.WorldPosition(world_x, world_y,
                                            orientation=orientation)
        self.size = _get_default_size() if size is None else size
        self.visible = visible
        self.active_sprite = active_sprite
        self._last_sprite = active_sprite

    def __str__(self):
        return self.name

    def get_grids(self) -> List[utils.Grid]:
        grids = set()
        if self.size.width == 1 and self.size.height == 1:
            grids.add(utils.Grid(self.position.y, self.position.x))
        else:
            for row in range(self.size.height):
                for col in range(self.size.width):
                    y = self.position.y + row
                    x = self.position.x + col
                    grids.add(utils.Grid(y, x))

        return grids

    def is_visible(self):
        return self.visible

    def set_active_sprite(self, sprite: Sprite) -> None:
        self.active_sprite = sprite

    def draw(self, canvas: tk.Canvas) -> None:
        if not self.visible:
            # TODO : Remove this, debug only.
            print('Not visible, not drawing')
            return

        self.active_sprite.draw(self.position, canvas)

        if (self.active_sprite is not self._last_sprite
           and self._last_sprite is not None):
            # Hide old sprite.
            self._last_sprite.hide(canvas)
            pass

        self._last_sprite = self.active_sprite

    def interract(self, action: Action) -> None:
        """ Interracts with the object.
        """
        pass

    def examine(self) -> ExamineResponse:
        """ Examines the object.
            Returns an ExamineResponse, which the invoker
            can use.
        """


def _get_name(name: str) -> str:
    if name is None:
        # Create new default name.
        name = f'Object {BaseObject._obj_id}'
        BaseObject._obj_id += 1

    return name


class EmptyObject(BaseObject):
    pass


class TargetObject(BaseObject):
    pass


class WallObject(BaseObject):

    def __init__(self, *args, **kwargs):
        sprite = SingleSprite('wall.png')
        super().__init__(*args, name='Wall', visible=True,
                         active_sprite=sprite, **kwargs)

    def draw2(self, canvas: tk.Canvas) -> None:
        size = utils.Settings.GRID_SIZE
        x = self.position.x*size + (size / 2)
        y = self.position.y*size + (size / 2)
        canvas.create_text(x, y, text='B', tag='path')

    def on_left_click(self):
        pass


class GridObject(BaseObject):

    def __init__(self, node, *args, **kwargs):
        self.node = node
        super().__init__(*args, **kwargs)

    def is_visible(self):
        return True

    def draw(self, canvas: tk.Canvas) -> None:
        size = utils.Settings.GRID_SIZE
        #pad = size / 3.5

        x = self.position.x*size + (size / 2)
        y = self.position.y*size + (size / 2)

        #canvas.create_text(x-pad, y-pad, text=self.node.g, tag='path', fill='green')
        #canvas.create_text(x+pad, y-pad, text=self.node.h, tag='path', fill='red')
        canvas.create_text(x, y, text='X', tag='path')
