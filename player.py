import pyxel as px

class Player:
    IMGX = 0
    IMGY = 0
    SIZE = px.TILE_SIZE * 2

    def __init__(self, pos):
        self.pos = pos

    def update(self):
        pass

    def draw(self):
        px.blt(self.pos.x, self.pos.y, 0, self.IMGX, self.IMGY, self.SIZE, self.SIZE, px.COLOR_BLACK)


    