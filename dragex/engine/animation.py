from collections import namedtuple
from typing import Dict, List
import time

from engine.sprite import Sprite, NullSprite
from engine.base_object import BaseObject


Transition = namedtuple('Transition', ['sprite', 'duration'])


class Animation:
    """ An animation consists of several transitions
        between sprites.
    """

    def __init__(self,
                 replay=True,
                 frames: List[Transition] = []):

        self.replay = replay
        self.frames = frames
        self.index = 0
        self.t0 = None

    def get_sprite(self) -> Sprite:
        return self.frames[self.index].sprite

    def update(self) -> None:
        if self.t0 is None:
            self.t0 = time.time()
        else:
            t1 = time.time()
            dt = t1 - self.t0

            if dt > self.frames[self.index].duration:
                self._next_frame()
                self.t0 = t1

    def _next_frame(self) -> None:
        if self.index+1 == len(self.frames) and self.replay:
            self.index = 0
        else:
            self.index += 1


class AnimationHandler:

    def __init__(self, obj: BaseObject):
        self._obj = obj
        self._animations: Dict[str, Animation] = {}
        self._curr_state = None

    def set_state(self, state: str) -> bool:
        if state not in self._animations:
            raise RuntimeError(f'Failed to find state {state}')
        self._curr_state = state

    def add_animation(self, state: str, animation: Animation) -> None:
        """ Adds an animation to the total animations, given
            a state to identify when the animation is suppose to
            be played.

            state:     A string that names the given animation.
            animation: The animation.
        """
        self._animations[state] = animation
        # Set default state
        if self._curr_state is None:
            self._curr_state = state

    def get_sprite(self) -> Animation:
        """ Returns the current active animation sprite.
            Returns none of there are no animations.
        """
        if self._curr_state is None:
            return NullSprite()

        anim = self._animations[self._curr_state]
        anim.update()
        return anim.get_sprite()
