import pyxel as px

class App:
    def __init__(self):
        px.init(160, 120)
        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        px.cls(0)

App()    