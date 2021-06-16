from utils import Singleton, Size
from engine.sprite import Sprite, SingleSprite
from engine.exceptions import NoSpriteExists

from typing import Dict


_DEFAULT_SPRITES = [
    'null'
]


class SpriteLoader(Singleton):

    def init(self):
        self._sprites: Dict[str, Sprite] = dict()
        self._load_default_sprites()

    def _load_default_sprites(self):
        for sprite in _DEFAULT_SPRITES:
            self._sprites[sprite] = SingleSprite(sprite, Size(1, 1))

    def _get_null_sprite(self) -> Sprite:
        return self._sprites['null']

    def get_sprite(self, sprite: str, size: Size = Size(1, 1)) -> Sprite:
        """ Returns the sprite with the given name.
            If the sprite can't be found, a NullSprite is returned.
        """
        print(f'Loading sprite: {sprite}')

        if sprite not in self._sprites:
            # If we fail to find the sprite, we probably haven't loaded it yet.
            try:
                new_sprite = SingleSprite(sprite, size)
                self._sprites[sprite] = new_sprite
            except NoSpriteExists:
                new_sprite = self._get_null_sprite()

            sprite = new_sprite
        else:
            sprite = self._sprites[sprite]

        return sprite
