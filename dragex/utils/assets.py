from PIL import Image
import os
import json

from .singleton import Singleton


BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BASE_PATH = os.path.join(BASE_PATH, 'assets')
NPC_BLUEPRINTS = 'npcs_blueprint.json'


class AssetHandler(Singleton):

    @staticmethod
    def open_image(asset: str):
        return Image.open(AssetHandler.path('images', asset))

    @staticmethod
    def open_sprite(asset: str) -> Image:
        return Image.open(AssetHandler.path('sprites', asset))

    @staticmethod
    def open_blueprints() -> dict:
        with open(os.path.join(BASE_PATH, NPC_BLUEPRINTS)) as f:
            return json.load(f)

    @staticmethod
    def open_asset(asset: str, image=True, mode='r'):
        if image:
            return Image.open(AssetHandler.path(asset))

    @staticmethod
    def path(*assets: str) -> str:
        return os.path.join(BASE_PATH, *assets)


class K(Singleton):
    pass


if __name__ == '__main__':
    ass1 = AssetHandler(1)
    ass2 = AssetHandler()
    k = K()
    print(ass1)
    print(ass2)
    print(k)
    print(ass1.open_image('man.png'))
