from collections import namedtuple
from PIL import Image

from exceptions import NoSpriteExists
from .assets import AssetHandler
from .settings import Settings
from .size import Size
from .position import Position

Dimension = namedtuple('Dimension', ['width', 'height'])
Coordinates = namedtuple('Coordinates', ['x', 'y'])


def _game_size_to_pixel_dimenions(size: Size) -> Dimension:
    """ Turns a game size into pixel dimensions.
        Returns a tuple of (width, height).
    """
    width = size.width * Settings.GRID_SIZE
    height = size.height * Settings.GRID_SIZE
    return Dimension(width, height)


def _game_position_to_pixel_coords(size: Size,
                                   position: Position) -> Coordinates:
    """ Turns game position, aka grid square position into
        pixel coordinates.
        Returns a tuple of (x, y).
    """
    x = position.x * Settings.GRID_SIZE + size.width*(Settings.GRID_SIZE / 2)
    y = position.y * Settings.GRID_SIZE + size.height*(Settings.GRID_SIZE / 2)

    return Coordinates(x, y)


def _get_image(source: str, size: Size) -> Image:
    org_source = source

    # Add proper extension if needed.
    if not source.endswith(Settings.SPRITE_EXTENSION):
        source += Settings.SPRITE_EXTENSION

    # Get the proper pixel size.
    pixel_size = _game_size_to_pixel_dimenions(size)

    # Load the image from disk.
    try:
        image = AssetHandler.open_sprite(source)
    except Exception:
        raise NoSpriteExists(f'Failed to load sprite {org_source}')

    # Resize the sprite to correct dimensions before returning.
    image = image.resize((pixel_size.width, pixel_size.height))
    return image
