# Le yin et le yang.
# https://edupython.tuxfamily.org/sources/view.php?code=yin

# Créé par VINNI, le 18/06/2013 avec EduPython
from lycee import *
import turtle as tortue

r = 100
tortue.up()
tortue.forward(r)
tortue.down()
tortue.left(90)
tortue.circle(2 * r)
tortue.circle(r, 180)
tortue.circle(-r, 180)
tortue.hideturtle()

tortue.mainloop()
