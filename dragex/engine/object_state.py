from engine.animation import AnimationHandler
from engine.event_queue import EventQueue
from engine import interact


class ObjectState:
    IDLE = 0
    MOVING = 1
    ATTACKING = 2
    DANCING = 3

    _STATE_STRINGS = {
        IDLE: 'IDLE',
        MOVING: 'MOVING',
        ATTACKING: 'ATTACKING',
        DANCING: 'DANCING'
    }

    def __init__(self, anim_handler: AnimationHandler, state: int = 0):
        self._anim_handler = anim_handler
        self._state = state
        self._event_queue = EventQueue()

    def set(self, state: int) -> None:
        self._state = state
        self._anim_handler.set_state(self._state)

        state_string = self._STATE_STRINGS[self._state]
        self._event_queue.add(interact.Status('state', state_string))

    def get(self) -> int:
        return self._state
