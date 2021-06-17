from interfaces.drawable import Drawable
from interfaces.screen import Screen
from . import gear


class PlayerGear(Drawable):

    def __init__(self):
        self.head: gear.Gear = gear.Sword()
        self.shoulders: gear.Gear = gear.Sword()
        self.sword: gear.Gear = gear.Sword()
        self.shield: gear.Gear = gear.Chest()
        self.chest: gear.Gear = gear.Sword()
        self.legs: gear.Gear = gear.Sword()
        self.cape: gear.Gear = gear.Sword()
        self.trinket: gear.Gear = gear.Sword()

        self._pieces = [
            self.head,
            self.shoulders,
            self.sword,
            self.shield,
            self.chest,
            self.legs,
            self.cape,
            self.trinket,
        ]

    def load(self):
        for piece in self._pieces:
            gear.load()

    def draw(self, screen: Screen) -> None:
        for piece in self._pieces:
            gear.draw(screen)
