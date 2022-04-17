import pyxel as px

class Level:
    def __init__(self, tilemap, startx, starty, goaly):
        self.tilemap = tilemap
        self.startx = startx
        self.starty = starty
        self.goaly = goaly
        self.x = 0
        self.y = 0
        self.started = False

    def start(self):
        self.started = True

    def draw(self):
        px.bltm(0, 0, self.tilemap, self.x, self.y, px.width, px.height, 0)

    def udpate(self):
        if self.started:
            self.x += 1
    
    def vitory(self):
        return self.y >= self.goaly