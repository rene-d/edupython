# Polynome dérivé
# https://edupython.tuxfamily.org/sources/view.php?code=derive

# Créé par IANTE, le 17/07/2011
from lycee import *
P=liste_demande("Entrez les coef du polynome, séparés par des virgules")
print ("Le polynôme dérivé de",affiche_poly(P),"est",end="")
d=1
while d<len(P):
    P[d]=d*P[d]
    d=d+1
P.pop(0)
print (affiche_poly(P))
