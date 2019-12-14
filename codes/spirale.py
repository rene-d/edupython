# Tracer une spirale.
# https://edupython.tuxfamily.org/sources/view.php?code=spirale

# Créé par VINNI, le 18/06/2013 avec EduPython
from lycee import *
import turtle as tortue

n = 10
for i in range(n):
    tortue.circle(5 * i, 90)

tortue.mainloop()
