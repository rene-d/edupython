# Dessiner un soleil
# https://edupython.tuxfamily.org/sources/view.php?code=soleil

# Créé par VINNI, le 18/06/2013 avec EduPython
from lycee import *
import turtle as tortue

i = 0
while i < 120:
    tortue.right(90)
    tortue.forward(100)
    tortue.right(180)
    tortue.forward(100)
    tortue.right(90)
    tortue.circle(50, 3)
    i = i + 1

tortue.mainloop()
