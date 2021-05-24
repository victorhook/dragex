from engine.animation import AnimationHandler


class NpcState:
    IDLE = 0
    MOVING = 1
    ATTACKING = 2
    DANCING = 3

    def __init__(self, anim_handler: AnimationHandler, state: int = 0):
        self._anim_handler = anim_handler
        self._state = state

    def set(self, state: int) -> None:
        self._state = state
        self._anim_handler.set_state(self._state)

    def get(self) -> int:
        return self._state
