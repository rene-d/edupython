# Volume d'eau dans une cuve
# https://edupython.tuxfamily.org/sources/view.php?code=cuve

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *

# On possède une cuve parallélépipédique de base rectangulaire
# (2m par 3m) et de 80 cm de hauteur.
# On cherche à savoir en fonction de la hauteur d'eau h,
# le volume d'eau dans la cuve.

h= demande("valeur de h en décimètres?")
if 0>h:                        # On teste si la valeur fournie par l'utilisateur
                               # est bien strictement positive
    print ("h est impossible")
if h>=0 and h<=8:              # On calcule le volume de la cuve si la valeur fournie
                               # par l'utilisateur ne dépasse pas la hauteur de la cuve.
    V= 600*h
    print ("le volume contenu dans la cuve est",V,"litres pour h=",h)
if h>8:                        # Dans ce cas, on affiche un message d'erreur.
    print ("la cuve déborde!!!")
