# Tracer un polygone régulier à n côtés.
# https://edupython.tuxfamily.org/sources/view.php?code=polygone

# Créé par VINNI, le 18/06/2013 avec EduPython
from lycee import *
import turtle as tortue

n = demande("Nombre de côtés (au moins 3)")
for i in range(n):
    tortue.forward(50)
    tortue.left(360 / n)

tortue.mainloop()
