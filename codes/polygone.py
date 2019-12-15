# Tracer un polygone régulier à n côtés.
# http://amienspython.tuxfamily.org/sources/codes/polygone.py

from lycee import *
n=demande("Nombre de côtés (au moins 3)")
for i in range(n):
    tortue.forward(50)
    tortue.left(360/n)
