# Volume d'eau dans une cuve
# http://amienspython.tuxfamily.org/sources/codes/cuve.py

from __future__ import division
from lycee import *

# On possède une cuve cuve parallélépipédique de base rectangulaire
# (2m par 3m) et de 80 cm de hauteur.
# On cherche à savoir en fonction de la hauteur d'eau h,
# le volume d'eau dans la cuve.

h = demande ("valeur de h en mètres?")

if 0 > h :                      # On teste si la valeur fournie par l'utilisateur
                                # est bien strictement positive
    print "h est impossible"

if h >= 0 and h <= 8 :          # On calcule le volume de la cuve si la valeur fournie
    V = 600 * h                 # par l'utilisateur ne dépasse pas la hauteur de la cuve.
                                # Dans ce cas, on affiche un message d'erreur.
    print "Le volume contenu dans la cuve est", V, "litres pour h=", h
if h > 8 :
    print "La cuve déborde!!!"
