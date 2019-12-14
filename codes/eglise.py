# Tracer une église
# https://edupython.tuxfamily.org/sources/view.php?code=eglise

# Créé par VINNI, le 18/06/2013 avec EduPython
from lycee import *
import turtle as tortue

tortue.left(90)
tortue.forward(100)
B = acosD(40 / 100)
tortue.right(90 - B)
tortue.forward(100)
C = 180 - 2 * B
tortue.right(180 - C)
tortue.forward(100)
tortue.right(90 - B)
tortue.forward(20)
tortue.left(90)
tortue.forward(100)
tortue.right(50)
FG = 20 / cosD(50)
tortue.forward(FG)
tortue.right(40)
HG=80 - sqrt(FG * FG - 20 * 20)
tortue.forward(HG)
tortue.right(90)
tortue.forward(200)

tortue.mainloop()
