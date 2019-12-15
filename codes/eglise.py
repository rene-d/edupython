# Tracer d'une église
# http://amienspython.tuxfamily.org/sources/codes/eglise.py

from lycee import *
tortue.reset()
tortue.left(90)
tortue.forward(100)
B=acos(40.0/100)
tortue.right(90-B)
tortue.forward(100)
C=180-2*B
tortue.right(180-C)
tortue.forward(100)
tortue.right(90-B)
tortue.forward(20)
tortue.left(90)
tortue.forward(100)
tortue.right(50)
FG=20/cos(40)
tortue.forward(FG)
tortue.right(40)
HG=80-sqrt(FG*FG-20*20)
tortue.forward(HG)
tortue.right(90)
tortue.forward(200)
