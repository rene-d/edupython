# Le drapeau européen.
# http://amienspython.tuxfamily.org/sources/codes/cee.py

from lycee import *
tortue.pensize(2)                       # Epaisseur du scripteur
tortue.pencolor(230, 230, 40)           # Couleur du scripteur
tortue.bgcolor('blue')                  # Couleur de fond
for etoile in range(12) :
    tortue.down()
    for branche in range(5) :
        tortue.forward(30)
        tortue.left(144)
    tortue.up()
    tortue.forward(50)                  # Calcul d'angle fait pour un dodécagone régulier
    tortue.left(30)                     # dont les côtés supportent les branches des étoiles.
