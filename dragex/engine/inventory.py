

class Item:

    def __init__(self, name: str, id: int = 0):
        self.name = name
        self.id = id


class Inventory:

    def __init__(self):
        self.max_capacity = 16
        self._items = []

    def add(self, item: Item) -> bool:
        if len(self._items) == self.max_capacity:
            return False
        self._items.append(item)
        return True

    def get(self) -> list:
        return self._items

    def move(self, item1: Item, item2: Item) -> None:
        i1 = self._items.index(item1)
        i2 = self._items.index(item2)
        self._items[i1] = item2
        self._items[i2] = item1
