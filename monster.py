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
    START_LIFE = 4
    NB_FRAME = 4

    def __init__(self, pos, level):
        super().__init__(pos, level)
        self.temp_death = False

    def reset(self, full = False):
        super().reset(full)
        self.temp_death = False

    def full_reset(self):
        self.life = self.START_LIFE

    def update(self):
        player_pos = self.level.player.pos
        if player_pos.x - px.width < self.pos.x < player_pos.x + px.width:
            super().update()

    @property
    def alive(self):
        return self.life > 0 and not self.temp_death

    def make_easier(self) -> None:
        self.life -= 1

if __name__ == "__main__":
    import main

    main.App()