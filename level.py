from turtle import pos
import pyxel as px
from typing import Union

from lib import Pos, posT, Rectangle
from player import Player

class Plateform:
    def __init__(self, imgs: Pos, pos:Pos, width: int) -> None:
        self.imgs = px.TILE_SIZE * imgs
        self.pos = px.TILE_SIZE * pos
        self.width = width
        self.rect = Rectangle(self.pos, self.width * px.TILE_SIZE, px.TILE_SIZE)

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


class killer:
    def __init__(self) -> None:
        self.pos = pos
class Level:
    IGNORE_TILE = [(0, 0), (4, 0)]
    def __init__(self, tilemap: Union[px.Tilemap, int], goaly: float):
        if isinstance(tilemap, int):
            self.tilemap = px.tilemap(tilemap)
        else:
            self.tilemap = tilemap
        self.goaly = goaly

        self.plateform = []
        self.killer = []

        self.init_from_tile_map()
    
    def start(self):
        self.pos = Pos(0, 0)

    def init_from_tile_map(self):
        plt_start = False
        for v in range(px.TILEMAP_SIZE):
            for u in range(px.TILEMAP_SIZE):
                tile = self.tilemap.pget(u, v)
                if tile in self.IGNORE_TILE:pass

                elif tile == (1, 0):
                    # start of plateform
                    assert not plt_start, f"starting twice ({u}, {v})"
                    plt_start = Pos(u, v)
                    plt_width = 1
                elif tile == (2, 0):
                    # plateform continuing
                    assert plt_start, f"continue without start ({u}, {v})"
                    plt_width += 1
                elif tile == (3, 0):
                    assert plt_start, f"end without start ({u}, {v})"
                    # stop of a plateform
                    self.plateform.append(Plateform(Pos(1, 0), plt_start, plt_width))
                    plt_start = False

                elif tile == (4, 1):
                    self.killer.append(Plateform(Pos(4, 1), Pos(u, v), 255))

                elif tile == (0, 1):
                    self.init_player = px.TILE_SIZE * Pos(u, v)
                    self.player = Player(self.init_player, self)
                else:
                    print("unkwon tile", tile, "at", u, ",", v)

    def draw(self):
        for plt in self.plateform:
            plt.draw()

        for kill in self.killer:
            kill.draw()

        self.player.draw()

    def udpate(self):
        self.player.update()

        camera_x = max(0, self.player.pos.x - 3 * px.TILE_SIZE)
        px.camera(camera_x, self.pos.y)
    
    def victory(self):
        return self.pos.y >= self.goaly


if __name__ == "__main__":
    import main

    main.App()