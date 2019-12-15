# Dessiner un soleil
# http://amienspython.tuxfamily.org/sources/codes/soleil.py

from lycee import *
i=0
while i<120:
    tortue.right(90)
    tortue.forward(100)
    tortue.right(180)
    tortue.forward(100)
    tortue.right(90)
    tortue.circle(50,3)
    i=i+1
