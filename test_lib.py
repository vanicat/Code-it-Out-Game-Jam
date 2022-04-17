from lib import Rectangle

def should_collide(r1, r2, msg):
    assert r1.collide(r2), f"{msg}: {r1} should collide with {r2}"
    assert r2.collide(r1), f"{msg}: {r2} should collide with {r1}"

def should_not_collide(r1, r2, msg):
    assert not r1.collide(r2), f"{msg}: {r1} should not collide with {r2}"
    assert not r2.collide(r1), f"{msg}: {r2} should not collide with {r1}"

def test_recangle_propreties():
    r1 = Rectangle(50, 60, 10, 20)

    assert r1.top == 60
    assert r1.bottom == 60 + 20
    assert r1.left == 50
    assert r1.right == 50 + 10

def test_collision():
    r1 = Rectangle(50, 60, 10, 20)

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