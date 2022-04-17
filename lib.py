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

    def copy(self):
        return Pos(self.x, self.y)

def posT(t):
    x, y = t
    return Pos(x, y)


class Rectangle:
    def __init__(self, *args):
        """*args must contain upper left coin and width and heigs
        
Both can be given as an tupple or a two number"""
        args = iter(args)
        n = next(args)
        if isinstance(n, tuple) or isinstance(n, Pos):
            self.x, self.y = n
        else: # Need to be a number
            self.x = n
            self.y = next(args)
        
        n = next(args)
        if isinstance(n, tuple) or isinstance(n, Pos):
            self.w, self.h = n
        else: # Need to be a number
            self.w = n
            self.h = next(args)

    @property
    def bottom(self):
        return self.y + self.h
    
    @property
    def top(self):
        return self.y

    @property
    def right(self):
        return self.x + self.w
    
    @property
    def left(self):
        return self.x

    def contain(self, p: Pos):
        return (
            self.left <= p.x < self.right and 
            self.top <= p.y < self.bottom 
        )

    def under(self, rect: "Rectangle"):
        return (
            rect.left <= self.right and 
            rect.right >= self.left and 
            self.top - 1 <= rect.bottom <= self.top + 2
        )

    def collide(self, rect: "Rectangle"):
        return (
            rect.left <= self.right and 
            rect.right >= self.left and 
            rect.top <= self.bottom and
            rect.bottom >= self.top
        )

    def __repr__(self):
        return f"Rectangle({self.x}, {self.y}, {self.w}, {self.h})"
