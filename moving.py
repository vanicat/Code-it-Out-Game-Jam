from abc import ABC, abstractmethod
import pyxel as px

from lib import Pos, Rectangle

class Moving(ABC):
    IMGX: int
    IMGY: int # may be a parameter
    HEIGHT: int
    WIDTH: int
    START_SPEED: Pos
    NB_FRAME: int

    def __init__(self, pos, level):
        self.init_pos = px.TILE_SIZE * pos
        self.level = level
        self.reset()

    @property
    @abstractmethod
    def alive(self):
        pass
    
    @abstractmethod
    def full_reset(self):
        pass

    def reset(self, full = False):
        self.pos = self.init_pos.copy()
        self.speed = self.START_SPEED.copy()

        self.started = False
        if full:
            self.full_reset()

    def start(self):
        self.started = True

    def update(self):
        if self.started:
            self.pos += self.speed

    def collide(self, rect):
        self.rect.collide(rect)

    @property
    def rect(self):
        return Rectangle(self.pos, self.WIDTH, self.HEIGHT)

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
        nbimg = (px.frame_count // 4) % self.NB_FRAME
        px.blt(self.pos.x, self.pos.y, 0, self.IMGX + self.WIDTH * nbimg, self.IMGY, self.WIDTH, self.HEIGHT, px.COLOR_BLACK)
