import pyxel as px
#from level import Level

from lib import Pos

class Player:
    IMGX = 0
    IMGY = 0
    SIZE = px.TILE_SIZE * 2
    GRAVITY = Pos(0, 2)
    JUMP = Pos(0, -6)
    NB_JUMP = 2
    JUMP_GRAVITY = 0.5
    START_SPEED = Pos(2, 0)

    def __init__(self, pos, level: "Level"):
        self.pos = pos
        self.level = level
        self.rect = self

        self.speed = self.START_SPEED.copy()

        self.jump = None
        self.jump_left = self.NB_JUMP

        self.started = False

    def start(self):
        self.started = True

    def update(self):
        if self.started:
            self.falling = True

            for plt in self.level.plateform:
                if plt.rect.under(self):
                    self.falling = False
                    self.jump = None
                    self.jump_left = self.NB_JUMP
                    self.bottom = plt.rect.top

            if self.falling:
                self.pos += self.GRAVITY

            self.pos += self.speed

            if px.btnp(px.KEY_SPACE) and (not self.falling or self.jump_left > 0):
                self.jump = self.JUMP.copy()
                self.jump_left -= 1

            if self.jump is not None:
                self.pos += self.jump
                self.jump.y += self.JUMP_GRAVITY
                if self.jump.y > 0:
                    self.jump = None
        else:
            if px.btnp(px.KEY_SPACE):
                self.start()

    @property
    def bottom(self):
        return self.pos.y + self.SIZE

    @bottom.setter
    def bottom(self, y):
        self.pos.y = y - self.SIZE

    @property
    def top(self):
        return self.pos.y
        
    @property
    def left(self):
        return self.pos.x
    
    @property
    def right(self):
        return self.pos.x + self.SIZE

    def draw(self):
        px.blt(self.pos.x, self.pos.y, 0, self.IMGX, self.IMGY, self.SIZE, self.SIZE, px.COLOR_BLACK)


if __name__ == "__main__":
    import main

    main.App()