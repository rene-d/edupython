# Obtenir 7
# http://amienspython.tuxfamily.org/sources/codes/des7.py

from __future__ import division
from lycee import *

# On cherche à connaître la fréquence du résultat 7 pour la somme
# lorsqu'on lance deux dés à 6 faces 100 000 fois chacun.
# j compte le nombre de 7 donc j / 100 000 est la fréquence cherchée
j = 0
for i in range (100000) :                       # Pour 100 000 lancers de 2 dés.
    s = randint (1, 6) + randint (1, 6)         # Une alternative consisterait en la demande
    if s == 7 :                                 # du nombre de lancers de dés.
        j = j + 1
f = j / 100000                                  # Pas d'espace pour séparer les milliers
print "Le 7 est sorti", j, "fois, donc a une fréquence égale à", f
