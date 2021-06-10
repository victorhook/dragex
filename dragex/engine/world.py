from utils import Singleton, AssetHandler
from engine.object_factory import ObjectFactory


class World:

    def __init__(self, world: dict):
        self.objects = []
        for obj in world:
            self.objects.append(ObjectFactory.create(obj))

    def __iter__(self) -> list:
        return self.objects


class RelativeWorld(World):
    pass


class AbsoluteWorld(World):
    pass


class WorldLoader(Singleton):

    @staticmethod
    def load() -> World:
        return World(AssetHandler.open_world())
