# signe d'un trinôme
# http://amienspython.tuxfamily.org/sources/codes/trinome2.py

from lycee import *
a, b, c = demande ("Entrez les coefficients du trinôme séparés par des virgules.")
delta = b * b - 4 * a * c
if delta < 0 :
    if a > 0 :
        print "P(x) > 0 pour tout réel x"
    if a < 0 :
        print "P(x) < 0 pour tout réel x"
if delta == 0 :
    if a > 0 :
        print "P(x) est positif pour tout réel x"
    if a < 0 :
        print "P(x) est négatif pour tout réel x"
if delta > 0 :
    if a > 0 :
        print "P(x) > 0 à l'extérieur des racines"
    if a < 0 :
        print "P(x) < 0 à l'extérieur des racines"
