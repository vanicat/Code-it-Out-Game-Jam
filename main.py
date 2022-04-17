import pyxel as px

import level
import menu 

class App:
    def __init__(self):
        px.init(160, 120)
        px.load("main.pyxres")

        self.levels = [menu.MainMenu(), level.Level(0, 250)]
        self._curlevel = 0

        px.run(self.update, self.draw)
    
    @property
    def curlevel(self):
        return self.levels[self._curlevel]

    def update(self):
        self.curlevel.udpate()
        if self.curlevel.victory():
            if self._curlevel + 1 < len(self.levels):
                self._curlevel += 1
            else:
                pass # victory !

    def draw(self):
        px.cls(0)
        self.curlevel.draw()

if __name__ == "__main__":
    App()