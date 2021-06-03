from engine.npc import Npc
from engine.object_state import ObjectState
from engine.animation import Animation, Transition, SingleSpriteAnimation
from engine.sprite import SingleSprite
from utils import Size


class Goblin(Npc):

    def __init__(self):
        super().__init__('Goblin', 'A nasty little creature.', hostile=True,
                         size=Size(1, 1))
