# Le drapeau européen.
# https://edupython.tuxfamily.org/sources/view.php?code=cee

# Créé par VINNI, le 18/06/2013 avec EduPython
from lycee import *
import turtle as tortue

tortue.pensize(2)
tortue.pencolor(0.9 , 0.9, 0.2)
tortue.bgcolor('blue')
for etoile in range(12):
  tortue.down()
  for branche in range(5):
      tortue.forward(30)
      tortue.left(144)
  tortue.up()
  tortue.forward(50)
  tortue.left(30)

tortue.mainloop()
