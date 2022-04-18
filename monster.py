import pyxel as px
import level

from lib import Pos

class Monster:
    IMGX = 0
    IMGY = px.TILE_SIZE * 4 # may be a parameter
    HEIGHT = 5
    WIDTH  = px.TILE_SIZE
    START_SPEED = Pos(-2, 0) # may be a parameter

    def __init__(self, pos):
        self.init_pos = px.TILE_SIZE * pos
        self.rect = self
        self.reset()


    def reset(self, full = False):
        self.pos = self.init_pos.copy()
        self.speed = self.START_SPEED.copy()

        self.started = False

    def start(self):
        self.started = True


    def update(self):
        if self.started:
            self.pos += self.speed

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
        nbimg = (px.frame_count // 4) % 4
        px.blt(self.pos.x, self.pos.y, 0, self.IMGX + self.WIDTH * nbimg, self.IMGY, self.WIDTH, self.HEIGHT, px.COLOR_BLACK)


if __name__ == "__main__":
    import main

    main.App()