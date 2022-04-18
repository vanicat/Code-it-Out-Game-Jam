import pyxel as px
from typing import Union, List

from lib import Pos, posT, Rectangle
import player

class Plateform:
    def __init__(self, imgs: Pos, pos:Pos, width: int, ended = True) -> None:
        self.imgs = px.TILE_SIZE * imgs
        self.pos = px.TILE_SIZE * pos
        self.width = width
        self.ended = ended

    @property
    def rect(self):
        return Rectangle(self.pos, self.width * px.TILE_SIZE, px.TILE_SIZE)

    def udpate(self) -> None:
        pass

    def draw(self) -> None:
        px.blt(self.pos.x, self.pos.y,
            1, self.imgs.x, self.imgs.y, px.TILE_SIZE, px.TILE_SIZE)
        for i in range(1, px.ceil(self.width) - int(self.ended)):
            px.blt(self.pos.x + px.TILE_SIZE * i, self.pos.y,
                1, self.imgs.x + px.TILE_SIZE, self.imgs.y, px.TILE_SIZE, px.TILE_SIZE)
        if self.ended:
            px.blt(self.pos.x + (self.width - 1) * px.TILE_SIZE, self.pos.y,
                   1, self.imgs.x + px.TILE_SIZE * 2, self.imgs.y, px.TILE_SIZE, px.TILE_SIZE)

    def under(self, rect: Rectangle) -> bool:
        return self.rect.under(rect)
    
    def collide(self, rect: Rectangle) -> bool:
        return self.rect.collide(rect)

class Level:
    IGNORE_TILE = [(0, 0), (4, 0)]
    plateform: List[Plateform]
    killer: List[Plateform]

    def __init__(self, tilemap: Union[px.Tilemap, int], goaly: float):
        if isinstance(tilemap, int):
            self.tilemap = px.tilemap(tilemap)
        else:
            self.tilemap = tilemap
        self.goaly = goaly

    
    def reset(self):
        px.load("assets/main.pyxres")
        self.surrender = False
        self.plateform = []
        self.killer = []

        self.init_from_tile_map()
        self.pos = Pos(0, 0)
        self.player.reset(True)

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
                    self.plateform.append(Plateform(Pos(1, 0), plt_start, plt_width + 1))
                    plt_start = False

                elif tile == (4, 1):
                    self.killer.append(Plateform(Pos(4, 1), Pos(u, v), 255, False))

                elif tile == (4, 2):
                    self.target = Plateform(Pos(4, 2), Pos(u, v), 1, False)

                elif tile == (0, 1):
                    self.player = player.Player(Pos(u, v), self)
                else:
                    print("unkwon tile", tile, "at", u, ",", v)

    def draw(self):
        for plt in self.plateform:
            plt.draw()

        for kill in self.killer:
            kill.draw()

        self.target.draw()

        self.player.draw()

    def udpate(self):
        self.player.update()

        camera_x = max(0, self.player.pos.x - 3 * px.TILE_SIZE)
        px.camera(camera_x, self.pos.y)

        if px.btnp(px.KEY_B):
            self.surrender = True
    
    def victory(self):
        return self.player.victory

    def defeat(self):
        return self.surrender


if __name__ == "__main__":
    import main

    main.App()