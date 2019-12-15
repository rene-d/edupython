# Calculer l'IMC
# http://amienspython.tuxfamily.org/sources/codes/IMC.py

from __future__ import division
from lycee import *
m=demande("masse en kilo : ")
t=demande("taille en mètre : ")
IMC=m/(t*t)
print "L'IMC est de : ",IMC
