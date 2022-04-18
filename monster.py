import pyxel as px
import level

from lib import Pos, Rectangle
from moving import Moving

class Monster(Moving):
    IMGX = 0
    IMGY = px.TILE_SIZE * 4 # may be a parameter
    HEIGHT = 5
    WIDTH  = px.TILE_SIZE
    START_SPEED = Pos(-2, 0) # may be a parameter
    START_LIFE = 10
    NB_FRAME = 4

    def __init__(self, pos, level):
        super().__init__(pos, level)

    def full_reset(self):
        self.life = self.START_LIFE


if __name__ == "__main__":
    import main

    main.App()