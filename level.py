import pyxel as px
from typing import Union, List

from lib import Pos, posT, Rectangle, Number
import player
import monster

class Plateform:
    GROW_ON_FAIL = 1/8
    width: Number

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

    def make_easier(self) -> None:
        self.width += self.GROW_ON_FAIL

class Wall:
    REDUCE_ON_FAIL = 1/8
    height: Number

    def __init__(self, imgs: Pos, pos:Pos) -> None:
        self.tile = imgs
        self.tpos = pos
        self.imgs = px.TILE_SIZE * imgs
        self.pos = px.TILE_SIZE * pos
        self.height = 1

    def grow(self):
        self.height += 1

    @property
    def rect(self):
        return Rectangle(self.pos, px.TILE_SIZE, self.height * px.TILE_SIZE)

    def udpate(self) -> None:
        pass

    def draw(self) -> None:
        for i in range(0, px.ceil(self.height)):
            px.blt(self.pos.x, self.pos.y + i * px.TILE_SIZE,
                1, self.imgs.x, self.imgs.y, px.TILE_SIZE, px.TILE_SIZE)

    def collide(self, rect: Rectangle) -> bool:
        return self.rect.collide(rect)

    def make_easier(self) -> None:
        self.pos.y += self.REDUCE_ON_FAIL * px.TILE_SIZE
        self.height -= self.REDUCE_ON_FAIL

class Level:
    IGNORE_TILE = [(0, 0), (4, 0), (5, 1)]
    WALL_TILE = [(4, 4)]
    plateform: List[Plateform]
    killer: List[Plateform]
    death_counter: int

    def __init__(self, tilemap: Union[px.Tilemap, int]):
        if isinstance(tilemap, int):
            self.tilemap = px.tilemap(tilemap)
        else:
            self.tilemap = tilemap
    
    def reset(self):
        px.load("assets/main.pyxres")
        self.surrender = False
        self.death_counter = 0
        self.plateform = []
        self.killer = []
        self.monster = []
        self.drawable = []
        self.updable = []
        self.wall: List[Wall] = []

        self.init_from_tile_map()
        self.pos = Pos(0, 0)
        self.player.reset(True)
        for m in self.monster:
            m.reset(True)

    def init_from_tile_map(self):
        plt_start = False
        for v in range(px.TILEMAP_SIZE):
            for u in range(px.TILEMAP_SIZE):
                tile = self.tilemap.pget(u, v)
                pos = Pos(u, v)
                
                if tile in self.IGNORE_TILE:pass

                elif tile == (1, 0):
                    # start of plateform
                    assert not plt_start, f"starting twice ({u}, {v})"
                    plt_start = pos
                    plt_width = 1
                elif tile == (2, 0):
                    # plateform continuing
                    assert plt_start, f"continue without start ({u}, {v})"
                    plt_width += 1
                elif tile == (3, 0):
                    assert plt_start, f"end without start ({u}, {v})"
                    # stop of a plateform
                    plt = Plateform(Pos(1, 0), plt_start, plt_width + 1)
                    self.drawable.append(plt)
                    self.plateform.append(plt)
                    plt_start = False

                elif tile == (4, 1):
                    kill = Plateform(Pos(4, 1), pos, 255, False)
                    self.drawable.append(kill)
                    self.killer.append(kill)

                elif tile == (4, 2):
                    target = Plateform(Pos(4, 2), pos, 1, False)
                    self.drawable.append(target)
                    self.target = target

                elif tile == (6, 0):
                    m = monster.Monster(pos, self)
                    self.drawable.append(m)
                    self.updable.append(m)
                    self.monster.append(m)

                elif tile == (0, 1):
                    self.player = player.Player(pos, self)
                    self.drawable.append(self.player) # player si updable, but must be update last
                elif tile in self.WALL_TILE:
                    ttype = posT(tile)
                    up = None
                    for w in self.wall:
                        if w.tile == ttype and w.tpos + Pos(0, 1) == pos:
                            up = w
                            break
                    if up is None:
                        wall = Wall(ttype, pos)
                        self.drawable.append(wall)
                        self.wall.append(wall)
                    else:
                        up.grow()
                else:
                    print("unkwon tile", tile, "at", u, ",", v)

    def draw(self):
        camera_x = max(0, self.player.pos.x - 3 * px.TILE_SIZE)
        px.camera(camera_x, self.pos.y)

        for drawable in self.drawable:
            drawable.draw()

        px.text(camera_x + 3, self.pos.y + 3, f"death: {self.death_counter}", px.COLOR_LIGHT_BLUE)
        

    def udpate(self):
        for updable in self.updable:
            updable.update()

        self.player.update()


        if px.btnp(px.KEY_B):
            self.surrender = True
    
    def start(self):
        for m in self.monster:
            m.start()

    def death(self, killer):
        px.play(0, 1)
        self.death_counter += 1
        for m in self.monster:
            m.reset()

        killer.make_easier()
        
        self.player.reset()


    def victory(self):
        return self.player.victory

    def defeat(self):
        return self.surrender


if __name__ == "__main__":
    import main

    main.App()
