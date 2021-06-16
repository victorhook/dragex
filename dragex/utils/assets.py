from PIL import Image
import os
import json

from .singleton import Singleton


BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BASE_PATH = os.path.join(BASE_PATH, 'assets')
BLUEPRINTS = os.path.join(BASE_PATH, 'blueprints')
FILE_WORLD = 'world.json'


class AssetHandler(Singleton):

    @staticmethod
    def _get_json_filename(file) -> dict:
        if not file.endswith('.json'):
            file += '.json'
        return file

    @staticmethod
    def _open_json(file) -> dict:
        file = AssetHandler._get_json_filename(file)
        with open(os.path.join(file)) as f:
            return json.load(f)

    @staticmethod
    def _save_json(data, file) -> dict:
        file = AssetHandler._get_json_filename(file)
        print(f'Saving {data} to {file}')
        with open(os.path.join(file), 'w') as f:
            return json.dump(data, f)

    @staticmethod
    def open_image(asset: str):
        return Image.open(AssetHandler.path('images', asset))

    @staticmethod
    def open_sprite(asset: str) -> Image:
        return Image.open(AssetHandler.path('sprites', asset))

    @staticmethod
    def open_world() -> dict:
        return AssetHandler._open_json(os.path.join(BASE_PATH, FILE_WORLD))

    @staticmethod
    def open_blueprint(name: str) -> dict:
        return AssetHandler._open_json(os.path.join(BLUEPRINTS, name))

    @staticmethod
    def save_blueprint(data: dict, name: str) -> dict:
        return AssetHandler._save_json(data, os.path.join(BLUEPRINTS, name))

    @staticmethod
    def open_asset(asset: str, image=True, mode='r'):
        if image:
            return Image.open(AssetHandler.path(asset))

    @staticmethod
    def path(*assets: str) -> str:
        return os.path.join(BASE_PATH, *assets)




if __name__ == '__main__':
    ass1 = AssetHandler(1)
    ass2 = AssetHandler()
    k = K()
    print(ass1)
    print(ass2)
    print(k)
    print(ass1.open_image('man.png'))
