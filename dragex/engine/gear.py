from engine.sprite import Sprite, EmptySprite, SingleSprite
from engine.object_state import ObjectState
from typing import Dict

class GearStats:
    pass


class Gear:

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
        idle = SingleSprite('sword.png')
        #attacking =

        super().__init__(GearStats(), {
            ObjectState.IDLE: idle,
            ObjectState.MOVING: idle,
            ObjectState.ATTACKING: idle,
        })


class Chest(Gear):

    def __init__(self):
        sprite = SingleSprite('man.png')
        super().__init__(GearStats(), {
            ObjectState.IDLE: sprite,
            ObjectState.MOVING: sprite,
            ObjectState.ATTACKING: sprite,
        })
