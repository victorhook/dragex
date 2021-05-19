

class Position:

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __init__(self, x: int = 0, y: int = 0, orienation: int = NORTH):
        self.x = x
        self.y = y
        self.orienation = orienation


class WorldPosition(Position):
    pass


class RelativePosition(Position):
    pass
