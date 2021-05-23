import tkinter as tk

import utils
from .sprite import Sprite
from .drawable import Drawable


def _get_default_size() -> utils.Size:
    return utils.Size(1, 1)


class BaseObject(Drawable):

    _obj_id = 0

    def __init__(self,
                 name: str = None,
                 desription: str = None,
                 world_x: int = 0,
                 world_y: int = 0,
                 visible: bool = True,
                 size: utils.Size = None,
                 active_sprite: Sprite = None,
                 ):
        self.name = _get_name(name)
        self.position = utils.WorldPosition(world_x, world_y)
        self.size = _get_default_size() if size is None else size
        self.visible = visible
        self.active_sprite = active_sprite

    def get_grid(self) -> utils.Grid:
        return utils.Grid(self.position.x, self.position.y)

    def move(self, x: int, y: int) -> None:
        self.position.x = x
        self.position.y = y

    def rotate(self, direction: int) -> None:
        self.position.orienation = direction

    def is_visible(self):
        return self.visible

    def draw(self, canvas: tk.Canvas) -> None:
        if not self.visible:
            # TODO : Remove this, debug only.
            print('Not visible, not drawing')
            return

        self.active_sprite.draw(self.position, canvas)

    def on_left_click(self):
        pass

    def on_right_click(self):
        pass


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
        sprite = Sprite(utils.Size(1, 1), 'wall.png')
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
        pad = size / 3.5

        x = self.position.x*size + (size / 2)
        y = self.position.y*size + (size / 2)

        #canvas.create_text(x-pad, y-pad, text=self.node.g, tag='path', fill='green')
        #canvas.create_text(x+pad, y-pad, text=self.node.h, tag='path', fill='red')
        canvas.create_text(x, y, text='X', tag='path')
