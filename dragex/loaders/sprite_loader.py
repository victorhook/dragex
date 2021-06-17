from typing import Dict

from engine.sprite import Sprite, SingleSprite, SpriteImage
from exceptions import NoSpriteExists
from utils import Singleton, Size, AssetHandler, get_logger

logger = get_logger()


class SpriteLoader(Singleton):

    def init(self):
        self._sprites: Dict[str, Sprite] = dict()

    def _get_null_sprite(self) -> Sprite:
        return self._sprites['null']

    def create_sprite(self, name: str, size: Size,
                      sprite: SpriteImage) -> Sprite:
        """ Abstract method. """
        pass

    def load_sprites(self) -> None:
        """ Loads all sprites from disk into memory. """
        sprites_loaded = 0
        sprite_blueprint = AssetHandler.open_blueprint('sprites')

        for sprite_spec in sprite_blueprint:
            sprite_name = sprite_spec['name']
            sprite_size = sprite_spec['size']

            try:
                sprite = AssetHandler.open_sprite(sprite_name)

                # Call abstract method to handle any platform specific
                # operations that are bound to the UI.
                sprite = self.create_sprite(
                    name=sprite_name,
                    size=Size(*sprite_size),
                    sprite=sprite,
                )
            except NoSpriteExists:
                sprite = self._get_null_sprite()

            self._sprites[sprite_name] = sprite
            sprites_loaded += 1
            logger.info(f'Sprites loaded: [{sprites_loaded}]')

            # TODO: Logging system here.

        logger.info(self._sprites)

    def get_sprite(self, sprite: str, size: Size = Size(1, 1)) -> Sprite:
        """ Returns the sprite with the given name.
            If the sprite can't be found, a NullSprite is returned.
        """
        return self._sprites[sprite]


if __name__ == '__main__':
    lo = SpriteLoader()
    lo.load_sprites()
