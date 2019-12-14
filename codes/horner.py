# Méthode de Hörner
# https://edupython.tuxfamily.org/sources/view.php?code=horner

# Créé par IANTE, le 12/07/2011
from lycee import *
P=liste_demande('entrez les coefficients de P(x) par ordre des puissances croissantes')
r=demande('Entrez une racine évidente')
Q=[0]*(len(P)-1)
v=0
for d in range(len(P)-2,-1,-1):
    v=P[d+1]+r*v
    Q[d]=v
print (affiche_poly(P)+'=('+affiche_poly([-r,1])+')('+affiche_poly(Q)+')')
