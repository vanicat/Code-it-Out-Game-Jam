import pyxel as px

from level import Level

class App:
    def __init__(self):
        px.init(160, 120)
        px.load("main.pyxres")

        self.levels = [Level(0, 250)]
        self._curlevel = 0

        px.run(self.update, self.draw)
    
    def curlevel(self):
        return self.levels[self._curlevel]

    def update(self):
        self.curlevel().udpate()
        if self.curlevel().vitory():
            if self._curlevel + 1 < len(self.levels):
                self._curlevel += 1
            else:
                pass # victory !

    def draw(self):
        px.cls(0)
        self.curlevel().draw()

if __name__ == "__main__":
    App()