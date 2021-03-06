from typing import Dict

from ..base_object import ObjectState
from engine.sprite import Sprite, SingleSprite
from loaders.sprite_loader import SpriteLoader
from interfaces.drawable import Drawable


class GearStats:
    pass


class Gear(Drawable):

    def __init__(self,
                 stats: GearStats,
                 sprites: Dict[int, Sprite] = dict()
                 ):
        self.stats = stats
        self._sprites = sprites

    def get_sprite(self, state: int) -> Sprite:
        return self._sprites[state]


class Sword(Gear):

    def __init__(self):
        return
        idle = SpriteLoader.instance().get_sprite('sword')

        super().__init__(GearStats(), {
            ObjectState.IDLE: idle,
            ObjectState.MOVING: idle,
            ObjectState.ATTACKING: idle,
        })


class Chest(Gear):

    def __init__(self):
        return
        sprite = SpriteLoader.instance().get_sprite('man')

        super().__init__(GearStats(), {
            ObjectState.IDLE: sprite,
            ObjectState.MOVING: sprite,
            ObjectState.ATTACKING: sprite,
        })
