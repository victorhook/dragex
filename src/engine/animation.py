from dataclasses import dataclass

from .sprite import Sprite


class Animation:
    """ An animation consists of several transitions
        between sprites.
    """

    def __init__(self, replay=True):
        self.replay = replay
        self.current_frame = 0
        self.sprites = []

    def get_duration(self) -> float:
        time = 0
        for transition in self.sprites:
            time += transition.duration
        return time

    def get_sprite(self, elapsed_time: float) -> Sprite:
        current_transition = self.sprites[self.current_frame]
        if elapsed_time > current_transition.duration:
            sprite = self._next_sprite()
        else:
            sprite = current_transition.end

    def _next_sprite(self) -> Sprite:
        if self.replay:
            if self.current_frame == len(self.sprites):
                self.current_frame = 0
            else:
                self.current_frame += 1

        return self.sprites[self.current_frame].end

    def _time_for_next_sprite(self) -> float:
        pass


@dataclass
class SpriteTransition:
    """ A transition is a change from 1 sprite to another. """
    start: Sprite
    end: Sprite
    duration: float
