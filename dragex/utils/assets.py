from PIL import Image
import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BASE_PATH = os.path.join(BASE_PATH, 'assets')


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class AssetHandler(Singleton):

    @staticmethod
    def open_asset(asset: str, image=True, mode='r'):
        if image:
            return Image.open(AssetHandler.path(asset))

    @staticmethod
    def path(asset: str) -> str:
        return os.path.join(BASE_PATH, asset)


if __name__ == '__main__':
    ass1 = AssetHandler(1)
    ass2 = AssetHandler()

    print(ass1.open_asset('man.png'))
