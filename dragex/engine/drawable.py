from engine.screen import Screen


class Drawable:

    def load(self):
        """ Loads required data into memory. """
        pass

    def update(self, elapsed_time: float) -> None:
        """ Updates any state that the object has. """
        pass

    def draw(self, screen: Screen) -> None:
        """ Draws somethings on the canvas. """
        pass
