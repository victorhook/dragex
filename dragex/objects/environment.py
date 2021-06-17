from .base_object import BaseObject


class Environment(BaseObject):

    def __init__(self, name: str, **kwargs):
        super().__init__(name, **kwargs)
