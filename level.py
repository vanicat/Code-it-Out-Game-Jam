import pyxel as px
from lib import Pos

class Plateforme:
    def __init__(self, imgstart, pos) -> None:
        self.imgstart = imgstart

class Level:
    def __init__(self, tilemap, goaly):
        self.tilemap = tilemap
        self.goaly = goaly
        self.pos = Pos(0, 0)
        self.started = False

    def start(self):
        self.started = True

    def draw(self):
        px.bltm(0, 0, self.tilemap, self.pos.x, self.pos.y, px.width, px.height, 0)

    def udpate(self):
        if self.started:
            self.pos.x += 1
    
    def vitory(self):
        return self.pos.y >= self.goaly