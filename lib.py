from dataclasses import dataclass
import typing
Number = typing.Union[int, float] 

@dataclass
class Pos:
    """Position or vector"""

    x: Number
    y: Number

    def __add__(self, p: "Pos") -> "Pos":
        return Pos(self.x + p.x, self.y + p.y)
    
    def __iadd__(self, p: "Pos") -> "Pos":
        self.x += p.x
        self.y += p.y
        return self

    def __rmul__(self, l: Number) -> "Pos":
        return Pos(self.x * l, self.y * l)

    def __imul__(self, l: Number) -> "Pos":
        self.x *= l
        self.y *= l
        return self

    def __iter__(self):
        yield self.x
        yield self.y

    def copy(self):
        return Pos(self.x, self.y)

def posT(t: typing.Tuple[Number, Number]) -> Pos:
    x, y = t
    return Pos(x, y)


class Rectangle:
    x: Number
    y: Number
    w: Number
    h: Number

    def __init__(self, *args) -> None:
        """*args must contain upper left coin and width and heigs
        
Both can be given as an tupple or a two number"""
        iargs = iter(args)
        n = next(iargs)
        if isinstance(n, tuple) or isinstance(n, Pos):
            self.x, self.y = n
        else: # Need to be a number
            self.x = n
            self.y = next(iargs)
        
        n = next(iargs)
        if isinstance(n, tuple) or isinstance(n, Pos):
            self.w, self.h = n
        else: # Need to be a number
            self.w = n
            self.h = next(iargs)

    @property
    def bottom(self) -> Number:
        return self.y + self.h
    
    @property
    def top(self) -> Number:
        return self.y

    @property
    def right(self) -> Number:
        return self.x + self.w
    
    @property
    def left(self) -> Number:
        return self.x

    def contain(self, p: Pos) -> bool:
        return (
            self.left <= p.x < self.right and 
            self.top <= p.y < self.bottom 
        )

    def under(self, rect: "Rectangle") -> bool:
        return (
            rect.left <= self.right and 
            rect.right >= self.left and 
            self.top - 1 <= rect.bottom <= self.top + 2
        )

    def collide(self, rect: "Rectangle") -> bool:
        return (
            rect.left <= self.right and 
            rect.right >= self.left and 
            rect.top <= self.bottom and
            rect.bottom >= self.top
        )

    def __repr__(self) -> str:
        return f"Rectangle({self.x}, {self.y}, {self.w}, {self.h})"
