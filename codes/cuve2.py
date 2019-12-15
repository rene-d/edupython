# La cuve avec fonction
# http://amienspython.tuxfamily.org/sources/codes/cuve2.py

from __future__ import division
from lycee import *
def V(h):                     # On définit une nouvelle fonction V
    if h<20 :                 # Même principe de disjonction de cas que dans le programme sans fonction
        R=h/2
        return 1/3*pi*R*R*h   # On renvoie le volume d'eau dans le premier cas
    else :
        Vcyl=1/3*pi*10*10*20
        Vcone=pi*10*10*(h-20)
        return Vcyl+Vcone     # On renvoie le volume d'eau dans le seconde cas

h=demande("hauteur d'eau ?")
print "Le volume est",V(h)    # Appel de la fonction V
