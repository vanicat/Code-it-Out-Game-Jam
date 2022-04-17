import pyxel as px
import level

from lib import Pos

class Player:
    IMGX = 0
    IMGY = px.TILE_SIZE * 2
    HEIGHT = px.TILE_SIZE * 2
    WIDTH  = px.TILE_SIZE
    GRAVITY = Pos(0, 2)
    JUMP = Pos(0, -6)
    NB_JUMP = 2
    JUMP_GRAVITY = 0.5
    START_SPEED = Pos(2, 0)
    GROW_ON_FAIL = 1/8

    def __init__(self, pos, level: "level.Level"):
        self.init_pos = pos
        self.level = level
        self.rect = self
        self.last_plt = None

        self.reset()


    def reset(self, full = False):
        self.pos = self.init_pos.copy()
        self.speed = self.START_SPEED.copy()

        self.jump = None
        self.jump_left = self.NB_JUMP

        self.started = False
        self.victory = False
        if full:
            self.life = 10

    def start(self):
        self.started = True
        self.falling = True


    def update(self):
        if self.started:
            was_falling = self.falling
            self.falling = True

            for plt in self.level.plateform:
                if plt.under(self):
                    if was_falling:
                        px.play(0,3)
                    self.falling = False
                    self.jump = None
                    self.jump_left = self.NB_JUMP
                    self.bottom = plt.rect.top
                    self.last_plt = plt


            for kill in self.level.killer:
                if kill.collide(self):
                    self.reset()
                    px.play(0, 1)
                    self.last_plt.width += self.GROW_ON_FAIL
                    self.life -= 1

            if self.level.target.collide(self):
                self.victory = True
                px.play(0, 2)

            if self.falling:
                self.pos += self.GRAVITY

            self.pos += self.speed

            if px.btnp(px.KEY_SPACE) and (not self.falling or self.jump_left > 0):
                self.jump = self.JUMP.copy()
                px.play(0, 0)
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
        return self.pos.y + self.HEIGHT

    @bottom.setter
    def bottom(self, y):
        self.pos.y = y - self.HEIGHT

    @property
    def top(self):
        return self.pos.y
        
    @property
    def left(self):
        return self.pos.x
    
    @property
    def right(self):
        return self.pos.x + self.WIDTH

    def draw(self):
        nbimg = (px.frame_count // 4) % 3
        px.blt(self.pos.x, self.pos.y, 0, self.IMGX + self.WIDTH * nbimg, self.IMGY, self.WIDTH, self.HEIGHT, px.COLOR_BLACK)


if __name__ == "__main__":
    import main

    main.App()