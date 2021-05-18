from dataclasses import dataclass


@dataclass
class Position:
    x: int = 0
    y: int = 0


class WorldPosition(Position):
    pass


class RelativePosition(Position):
    pass
