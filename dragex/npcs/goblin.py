from engine.npc import Npc
from engine.object_state import ObjectState
from engine.animation import Animation, Transition, SingleSpriteAnimation
from engine.sprite import Sprite
from utils import Size


_GOBLIN_SPRITE = None


def load_sprite():
    global _GOBLIN_SPRITE
    _GOBLIN_SPRITE = Sprite(Size(1, 1), 'goblin.png')


class Goblin(Npc):

    def __init__(self):
        load_sprite()
        super().__init__('Goblin', 'A nasty little creature.')
        self.anim_handler.add_animation(ObjectState.IDLE,
                                        SingleSpriteAnimation(_GOBLIN_SPRITE))
