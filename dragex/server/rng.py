from engine.loot import Loot


class Rng:

    def __init__(self, seed: int = 0):
        self._seed = seed

    def spawn_loot(self) -> Loot:
        pass
