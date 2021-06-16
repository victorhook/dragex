from engine.object_controllable import ControllableGameObject
from engine.object_state import ObjectState
from engine.animation import Animation, Transition, AnimationHandler
from engine.screen import Screen
from engine.sprite import Sprite, SpriteCollection, SingleSprite

from player.player_gear import PlayerGear
from player.player_stats import PlayerStats


def _get_sprite(state: int, gear: PlayerGear) -> Sprite:
    sprites = SpriteCollection()
    for piece in gear:
        sprites.add(piece.get_sprite(state))
    return sprites


def _add_player_animations(state: int, anim_handler: AnimationHandler,
                           gear: PlayerGear) -> None:
    sprite = _get_sprite(state, gear)

    idle = Animation(frames=[Transition(sprite, 0.1)])
    moving = idle
    attacking = idle

    anim_handler.add_animation(ObjectState.IDLE, idle)
    anim_handler.add_animation(ObjectState.MOVING, moving)
    anim_handler.add_animation(ObjectState.ATTACKING, attacking)


class Player(ControllableGameObject):

    def __init__(self, name: str, **kwargs):
        self.gear: PlayerGear = PlayerGear()
        self.stats: PlayerStats = PlayerStats()
        """
            head
            shoulders
            sword
            shield
            chest
            legs
            cape
            trinket
        """
        super().__init__(name, world_x=10, world_y=10, speed=5, **kwargs,)

    def serialize(self):
        return {
            **super().serialize(),
            'hp': self.hp,
            'level': self.level,
            'state': self.state,
            'gear': self.gear,
        }

    def load_sprites(self):
        _add_player_animations(self.state.get(), self.anim_handler, self.gear)

    def draw(self, screen: Screen) -> None:
        super().draw(screen)

    def update(self, elapsed_time: float) -> None:
        self.ctrl.move(elapsed_time)
