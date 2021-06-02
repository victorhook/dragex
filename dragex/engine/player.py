import tkinter as tk

from engine.object_controllable import ControllableGameObject
from engine import gear
from engine.object_state import ObjectState
from engine.animation import Animation, Transition, AnimationHandler
from engine.sprite import Sprite, SpriteCollection, SingleSprite
import utils


class PlayerGear:

    def __init__(self):
        self.head: gear.Gear = gear.Sword()
        self.shoulders: gear.Gear = gear.Sword()
        self.sword: gear.Gear = gear.Sword()
        self.shield: gear.Gear = gear.Chest()
        self.chest: gear.Gear = gear.Sword()
        self.legs: gear.Gear = gear.Sword()
        self.cape: gear.Gear = gear.Sword()
        self.trinket: gear.Gear = gear.Sword()

        self._pieces = [
            self.head,
            self.shoulders,
            self.sword,
            self.shield,
            self.chest,
            self.legs,
            self.cape,
            self.trinket,
        ]

    def __iter__(self) -> gear.Gear:
        return self._pieces.__iter__()


class PlayerStats:

    def __init__(self):
        self.strength: int = 0
        self.agility: int = 0
        self.magic: int = 0
        self.archery: int = 0
        self.defence: int = 0
        self.stamina: int = 0
        self.critical_strike: int = 0
        self.speed: int = 0


def get_sprite(state: int, gear: PlayerGear) -> Sprite:
    sprites = SpriteCollection()
    for piece in gear:
        sprites.add(piece.get_sprite(state))
    return sprites


def add_animations(state: int, anim_handler: AnimationHandler,
                   gear: PlayerGear) -> None:
    sprite = get_sprite(state, gear)

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
        add_animations(self.state.get(), self.anim_handler, self.gear)

    def draw(self, canvas: tk.Canvas) -> None:
        super().draw(canvas)

    def update(self, elapsed_time: float) -> None:
        self.ctrl.move(elapsed_time)
