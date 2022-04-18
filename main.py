import pyxel as px

import level
import menu 

class App:
    def __init__(self):
        px.init(160, 120)
        px.load("assets/main.pyxres")

        self.levels:list[level.Level] = [menu.MainMenu(), level.Level(0, 250), menu.Victory()]
        self._curlevel = 0
        self.curlevel.reset()

        px.run(self.update, self.draw)
    
    @property
    def curlevel(self):
        return self.levels[self._curlevel]

    @curlevel.setter
    def curlevel(self, new):
        self._curlevel = new
        px.camera()
        self.curlevel.reset()

    def update(self):
        self.curlevel.udpate()
        if self.curlevel.victory():
            self.curlevel = (self._curlevel + 1) % len(self.levels)
        elif self.curlevel.defeat():
            self.curlevel = 0

    def draw(self):
        px.cls(0)
        self.curlevel.draw()

if __name__ == "__main__":
    App()