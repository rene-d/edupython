# Polynome dérivé
# http://amienspython.tuxfamily.org/sources/codes/derive.py

# Créé par IANTE, le 17/07/2011
from __future__ import division
from lycee import *
P=liste_demande("Entrez les coef du polynome, séparés par des virgules")
print "Le polynôme dérivé de",affiche_poly(P),"est",
d=1
while d<len(P):
    P[d]=d*P[d]
    d=d+1
P.pop(0)
print affiche_poly(P)
