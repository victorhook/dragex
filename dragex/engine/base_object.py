import utils
from .sprite import Sprite


class BaseObject:

    def __init__(self, rel_x: int = 0, rel_y: int = 0,
                 world_x: int = 0, world_y: int = 0,
                 size: tuple = (8, 8)):
        self.pos_relative = utils.RelativePosition(rel_x, rel_y)
        self.pos_absolute = utils.WorldPosition(world_x, world_y)
        self.size = utils.Size(*size)
        self.visible = False
        self.sprites = []
        self.active_sprite: Sprite = None

    def add_sprite(self, sprite: Sprite) -> None:
        self.sprites.append(sprite)

    def get_sprites(self) -> list:
        return self.sprites
