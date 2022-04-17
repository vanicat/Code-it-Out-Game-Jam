import pyxel as px
from lib import Pos
from typing import Union

class Plateform:
    def __init__(self, imgs: int, pos:Pos, width: int) -> None:
        self.imgs = imgs
        self.pos = px.TILE_SIZE * pos
        self.width = width

    def udpate(self) -> None:
        pass

    def draw(self) -> None:
        px.blt(self.pos.x, self.pos.y,
            1, self.imgs.x, self.imgs.y, px.TILE_SIZE, px.TILE_SIZE)
        for i in range(1, self.width - 1):
            px.blt(self.pos.x + px.TILE_SIZE * i, self.pos.y,
                1, self.imgs.x + px.TILE_SIZE, self.imgs.y, px.TILE_SIZE, px.TILE_SIZE)
        px.blt(self.pos.x + (self.width - 1) * px.TILE_SIZE, self.pos.y,
               1, self.imgs.x + px.TILE_SIZE * 2, self.imgs.y, px.TILE_SIZE, px.TILE_SIZE)
        



class Level:
    def __init__(self, tilemap: Union[px.Tilemap, int], goaly: float):
        if isinstance(tilemap, int):
            self.tilemap = px.tilemap(tilemap)
        else:
            self.tilemap = tilemap
        self.goaly = goaly
        self.pos = Pos(0, 0)
        self.plateform = [Plateform(Pos(8, 0), self.pos, 3)]
        self.started = False

    def start(self):
        self.started = True

    def draw(self):
        px.bltm(0, 0, self.tilemap, self.pos.x, self.pos.y, px.width, px.height, 0)
        for plt in self.plateform:
            plt.draw()

    def udpate(self):
        if self.started:
            self.pos.x += 1
    
    def vitory(self):
        return self.pos.y >= self.goaly