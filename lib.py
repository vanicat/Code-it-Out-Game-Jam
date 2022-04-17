from dataclasses import dataclass

@dataclass
class Pos:
    """Position or vector"""

    x: float
    y: float

    def __add__(self, p: "Pos"):
        return Pos(self.x + p.x, self.y + p.y)
    
    def __iadd__(self, p: "Pos"):
        self.x += p.x
        self.y += p.y
        return self

    def __rmul__(self, l: float):
        return Pos(self.x * l, self.y * l)

    def __imul__(self, l: float):
        self.x *= l
        self.y *= l
        return self

    def __iter__(self):
        yield self.x
        yield self.y

def posT(t):
    x, y = t
    return Pos(x, y)