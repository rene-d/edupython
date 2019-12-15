# PGCD récursif
# http://amienspython.tuxfamily.org/sources/codes/pgcd.py

from __future__ import division
from lycee import *

# On utilise l'algorithme d'Euclide pour déterminer le PGCD de a et b.

a, b = input ("Entrez deux entiers strictement positifs.")
                                          # L'utilisateur doit saisir les nombres séparés par une virgule
print "PGCD(", a, ", ", b, ") = ",
while b <> 0 :                            # La condition de poursuite de la boucle :
    a, b = b, reste (a, b)                # tant que le reste de la division n'est pas nul.
print a
