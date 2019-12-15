# Recherche d'un triplet pythagoricien d'entiers consécutifs
# http://amienspython.tuxfamily.org/sources/codes/pythagoricien.py

from __future__ import division
from lycee import *
for i in range(100000) :             # On va tester avec la réciproque de Pythagore
                                     # pour des nombres consécutifs compris entre 0 et 100001
    a = i * i + (i + 1) * (i + 1)    # Le carré de i peut être obtenu aussi en posant i**2 ou puissance(i, 2)
    r = (i + 2) * (i + 2)
    if r == a :
        print "Les nombres", i, ", ", i+1, "et", i + 2, "forment un triplet pythagoricien."
