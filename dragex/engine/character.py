from .base_object import BaseObject
from .object_controller import ObjectController


class Character(BaseObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctrl = ObjectController(self.position)
