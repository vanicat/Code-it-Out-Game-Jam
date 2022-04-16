import pyxel as px

from level import Level
class App:
    def __init__(self):
        px.init(160, 120)
        px.load("main.pyxres")

        self.levels = [Level(0, 10, 10, 250)]
        self.curlevel = 0

        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        px.cls(0)
        self.levels[self.curlevel].draw()
        
App()    