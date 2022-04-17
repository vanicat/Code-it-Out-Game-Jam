import pyxel as px

from lib import Pos

class Player:
    IMGX = 0
    IMGY = 0
    SIZE = px.TILE_SIZE * 2
    GRAVITY = Pos(0, 2)

    def __init__(self, pos, level: "Level"):
        self.pos = pos
        self.level = level

    def update(self):
        if self.falling():
            self.pos += self.GRAVITY

    def falling(self):
        return True

    def draw(self):
        px.blt(self.pos.x, self.pos.y, 0, self.IMGX, self.IMGY, self.SIZE, self.SIZE, px.COLOR_BLACK)



if __name__ == "__main__":
    import main

    main.App()