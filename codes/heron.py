# Calculer l'aire d'un triangle avec la formule de Héron
# http://amienspython.tuxfamily.org/sources/codes/heron.py

from __future__ import division
from lycee import *
# calcul de l'aire d'un triangle avec la formule de Héron
a, b, c = demande ("Entrez les longueurs des 3 côtés du triangle séparées par des virgules.")
p = (a + b + c) / 2                         #p est le demi périmètre du triangle
aire = sqrt (p * (p - a) * (p - b) * (p - c))
print "L'aire de ce triangle est", aire
