import pyxel as px
import level

from lib import Pos
from moving import Moving

class Player(Moving):
    IMGX = 0
    IMGY = px.TILE_SIZE * 2
    HEIGHT = px.TILE_SIZE * 2
    WIDTH  = px.TILE_SIZE
    GRAVITY = Pos(0, 2)
    JUMP = Pos(0, -6)
    NB_JUMP = 2
    JUMP_GRAVITY = 0.5
    START_SPEED = Pos(2, 0)
    NB_FRAME = 3
    last_plt: "level.Plateform"

    def __init__(self, pos, level: "level.Level"):
        super().__init__(pos, level)

    def full_reset(self):
        pass

    @property
    def alive(self):
        return True

    def reset(self, full = False):
        super().reset(full)

        self.jump = None
        self.jump_left = 0

        self.victory = False

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
                    self.level.death(self.last_plt)

            for monster in self.level.monster:
                if monster.under(self):
                    px.play(0, 4)
                    monster.temp_death = True
                elif monster.collide(self):
                    self.level.death(monster)

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
                self.level.start()

if __name__ == "__main__":
    import main

    main.App()