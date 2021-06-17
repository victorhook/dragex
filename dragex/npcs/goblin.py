from objects import Npc
from objects import ObjectState
from engine.animation import Animation, Transition, SingleSpriteAnimation
from engine.sprite import SingleSprite
from utils import Size


class Goblin(Npc):

    def __init__(self, *args, **kwargs):
        kwargs['name'] = 'Goblin'
        kwargs['description'] = 'A nasty little creature.'
        kwargs['size'] = Size(1, 1)
        kwargs['hostile'] = True
        super().__init__(*args, **kwargs)
