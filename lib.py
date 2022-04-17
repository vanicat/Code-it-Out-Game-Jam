from dataclasses import dataclass

@dataclass
class Pos:
    """Position or vector"""

    x: float
    y: float

    def __add__(self, p: "Pos"):
        Pos(self.x + p.x, self.y + p.y)
    
    def __iadd__(self, p: "Pos"):
        self.x += p.x
        self.y += p.y

    def __rmul__(self, l: float):
        Pos(self.x * l, self.y * l)

    def __imul__(self, l: float):
        self.x *= l
        self.y *= l