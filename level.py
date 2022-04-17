import pyxel as px
from typing import Union

from lib import Pos, posT, Rectangle
from player import Player

class Plateform:
    def __init__(self, imgs: Pos, pos:Pos, width: int) -> None:
        self.imgs = imgs
        self.pos = pos
        self.width = width
        self.rect = Rectangle(self.pos, self.width * px.TILE_SIZE, self.width * px.TILE_SIZE)

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

        self.plateform = []

        self.init_from_tile_map()

        self.started = False

    def init_from_tile_map(self):
        plt_start = False
        for u in range(px.TILEMAP_SIZE):
            for v in range(px.TILEMAP_SIZE):
                tile = self.tilemap.pget(u, v)
                if tile == (0, 0):pass
                elif tile == (1, 0):
                    # start of plateform
                    plt_start = (u, v)
                    plt_width = 1
                elif tile == (2, 0):
                    # plateform continuing
                    assert plt_start
                    plt_width += 1
                elif tile == (3, 0):
                    assert plt_start
                    # stop of a plateform
                    self.plateform.append(Plateform(Pos(8, 0), px.TILE_SIZE * posT(plt_start), plt_width))
                    plt_start = False
                elif tile == (0, 1):
                    self.player = Player(px.TILE_SIZE * Pos(u, v), self)
                else:
                    print("unkwon tile", tile, "at", u, ",", v)

    def start(self):
        self.started = True

    def draw(self):
        for plt in self.plateform:
            plt.draw()
        self.player.draw()

    def udpate(self):
        if self.started:
            self.pos.x += 1
        self.player.update()
    
    def vitory(self):
        return self.pos.y >= self.goaly


if __name__ == "__main__":
    import main

    main.App()