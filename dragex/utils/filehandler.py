import json
from pathlib import Path

try:
    from .singleton import Singleton
except:
    from singleton import Singleton


BASE_PATH = Path.home().joinpath('.dragex')


class FileHandler(Singleton):

    def __init__(self):
        self.base = BASE_PATH
        if not self.base.exists():
            self.base.mkdir()

    def file_exists(self, filename: str) -> bool:
        return self.base.joinpath(filename).exists()

    def save(self, filename: str, data: str) -> None:
        dtype = type(data)
        with open(self.base.joinpath(filename), 'w') as f:
            if dtype is str:
                f.write(data)
            elif dtype is dict:
                json.dump(data, f)

    def open(self, filename: str, is_json: bool = False) -> str:
        with open(self.base.joinpath(filename)) as f:
            if is_json:
                return json.load(f)
            return f.read()
