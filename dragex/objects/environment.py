from dragex.engine.serialize import Serializable
from dragex.engine.base_object import BaseObject


class Environment(BaseObject, Serializable):

    def __init__(self, name: str, **kwargs):
        super().__init__(name, **kwargs)

