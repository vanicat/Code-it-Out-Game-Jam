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
        self.rect = self
        self.speed = Pos(2, 0)
        self.jump = None

    def update(self):
        self.falling = True
        
        for plt in self.level.plateform:
            if plt.rect.under(self):
                self.falling = False
                self.bottom = plt.rect.top
        
        if self.falling:
            self.pos += self.GRAVITY

        self.pos += self.speed

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