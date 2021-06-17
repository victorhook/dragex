from loaders.sprite_loader import SpriteLoader
from engine.sprite import Sprite, SpriteImage
from .tk_sprite import TkSprite
from utils import Size


class TkSpriteLoader(SpriteLoader):

    def create_sprite(self, name: str, size: Size,
                      sprite: SpriteImage) -> Sprite:
        return TkSprite(name, size, sprite)
