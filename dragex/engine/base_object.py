import tkinter as tk

import utils
from .sprite import Sprite
from .drawable import Drawable


def _get_default_size() -> utils.Size:
    return utils.Size(1, 1)


class BaseObject(Drawable):

    __obj_id = 0

    def __init__(self, name: str = None,
                 world_x: int = 0, world_y: int = 0,
                 size: utils.Size = None):
        self.name = _get_name(name)
        self.position = utils.WorldPosition(world_x, world_y)
        self.size = _get_default_size() if size is None else size
        self.visible = False
        self.sprites = []
        self.active_sprite: Sprite = None

    def add_sprite(self, sprite: Sprite) -> None:
        self.sprites.append(sprite)

    def get_sprites(self) -> list:
        return self.sprites

    def draw(self, canvas: tk.Canvas) -> None:
        if not self.visible:
            # TODO : Remove this, debug only.
            print('Not visible, not drawing')
            return

        self.active_sprite.draw(self.position, canvas)


def _get_name(name: str) -> str:
    if name is None:
        # Create new default name.
        name = f'Object {BaseObject.__obj_id}'
        BaseObject.__obj_id += 1

    return name
