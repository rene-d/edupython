# Tracer un oeuf de pâques.
# https://edupython.tuxfamily.org/sources/view.php?code=oeuf

# Créé par VINNI, le 18/06/2013 avec EduPython
from lycee import *
import turtle as tortue

r = 100
tortue.right(90)
tortue.circle(r, 180)
tortue.circle(2 * r, 45)
tortue.circle(r * (2 - sqrt(2)), 90)
tortue.circle(2 * r, 45)

tortue.mainloop()
