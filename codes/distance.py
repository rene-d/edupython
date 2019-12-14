# Distance sur un axe gradué
# https://edupython.tuxfamily.org/sources/view.php?code=distance

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *

# Ce programme donne la distance entre deux points distincts
# placés sur une droite graduée

xA=demande("Entrez l'abscisse du point A")
xB=demande("Entrez l'abscisse du point B")
if xA>xB :       # On teste le signe de la différence des abscisses de A et de B
    dist=xA-xB   # afin que le résultat fourni soit positif
else :
    dist=xB-xA
print ("La distance AB est",dist)
