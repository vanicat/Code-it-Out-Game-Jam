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


if __name__ == "__main__":
    def should_collide(r1, r2, msg):
        assert r1.collide(r2), f"{msg}: {r1} should collide with {r2}"
        assert r2.collide(r1), f"{msg}: {r2} should collide with {r1}"

    def should_not_collide(r1, r2, msg):
        assert not r1.collide(r2), f"{msg}: {r1} should not collide with {r2}"
        assert not r2.collide(r1), f"{msg}: {r2} should not collide with {r1}"

    r1 = Rectangle(50, 60, 10, 20)

    assert r1.top == 60
    assert r1.bottom == 60 + 20
    assert r1.left == 50
    assert r1.right == 50 + 10

    r_gauche = Rectangle(30, 60, 10, 15)
    r_gauche_mil = Rectangle(30, 63, 21, 15)
    r_gauche_droite = Rectangle(30, 63, r1.right + 2, 15)
    r_hmil = Rectangle(51, 63, 3, 15)
    r_mil_droite = Rectangle(51, 63, 21, 15)
    r_droite = Rectangle(61, 63, 21, 15)

    r_haut = Rectangle(51, 30, 8, 20)
    r_haut_mil = Rectangle(51, 30, 8, 31)
    r_haut_bas = Rectangle(51, 30, 8, 80)
    r_vmil = Rectangle(51, 61, 8, 10)
    r_mil_bas = Rectangle(51, 61, 8, 40)
    r_bas = Rectangle(51, 90, 8, 30)

    should_not_collide(r1, r_gauche, "gauche")
    should_collide(r1, r_gauche_mil, "gauche_mil")
    should_collide(r1, r_gauche_droite, "gauche_droite")
    should_collide(r1, r_hmil, "hmil")
    should_collide(r1, r_mil_droite, "mil droite")
    should_not_collide(r1, r_droite, "droite")

    should_not_collide(r1, r_haut, "haut")
    should_collide(r1, r_haut_mil, "haut_mil")
    should_collide(r1, r_haut_bas, "haut bas")
    should_collide(r1, r_vmil, "vmil")
    should_collide(r1, r_mil_bas, "mil_bas")
    should_not_collide(r1, r_bas, "bas")