import pyxel as px

import level
import menu 

class App:
    def __init__(self):
        px.init(160, 120)
        px.load("assets/main.pyxres")

        self.levels:list[level.Level] = [
            menu.MainMenu(),
            level.Level(0),
            level.Level(1),
            menu.Victory()
        ]
        self._curlevel = 0
        self.curlevel.reset(0)

        px.run(self.update, self.draw)
    
    @property
    def curlevel(self):
        return self.levels[self._curlevel]

    def set_curlevel(self, new, score):
        self._curlevel = new
        px.camera()
        if score is True:
            score = 0
        self.curlevel.reset(score)

    def update(self):
        self.curlevel.udpate()
        v = self.curlevel.victory()
        if v:
            self.set_curlevel((self._curlevel + 1) % len(self.levels), v)
        elif self.curlevel.defeat():
            self.set_curlevel(0, 0)

    def draw(self):
        px.cls(0)
        self.curlevel.draw()

if __name__ == "__main__":
    App()