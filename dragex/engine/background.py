from utils import Grid
from engine.sprite import Sprite


class Background:

    def __init__(self, grid: Grid, sprite: Sprite):
        self.grid = grid
        self.sprite = sprite
    
    def to_json(self) -> dict:
        
        return {
            f'{self.grid.row}{self.grid.col}': self.sprite.id
        }