# Recherche des entiers distincts tels que x^y=y^x
# https://edupython.tuxfamily.org/sources/view.php?code=puissance

# On cherche les entiers naturels qui vérifient x^y = y^x
    # On se limite aux entiers inférieurs à 100
from lycee import *
for x in range (1, 100) :
    for y in range (x + 1, 100) :
        if puissance (x, y) == puissance (y, x) :     # On peut écrire x**y au lieu de puissance (x, y)
            print (x, "^", y, "=", y, "^", x)
