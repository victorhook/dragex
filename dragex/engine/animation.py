from collections import namedtuple
from typing import Dict, List
import time

from engine.sprite import Sprite, NullSprite
from utils import get_logger


Transition = namedtuple('Transition', ['sprite', 'duration'])
logger = get_logger()


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


class SingleSpriteAnimation(Animation):
    """ Animation that only holds a single sprite, with no transitions. """

    def __init__(self, sprite: Sprite):
        self._sprite = sprite

    def get_sprite(self) -> Sprite:
        return self._sprite

    def update(self) -> None:
        pass


class AnimationHandler:

    def __init__(self):
        self._animations: Dict[int, Animation] = {}
        self._curr_state = None

    def set_state(self, state: int) -> bool:
        if state not in self._animations:
            logger.warning(f'Failed to load animation in state: {state}')
            #raise RuntimeError(f'Failed to find state {state}')

            # TODO: Better implementation for this.
            # Temporary fix.
            if self._curr_state is not None:
                self._animations[state] = self._animations[self._curr_state]

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
