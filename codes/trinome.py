# nombre de zéros d'un trinôme
# http://amienspython.tuxfamily.org/sources/codes/trinome.py

from lycee import *
a, b, c = demande ("Entrez les coefficients du trinôme séparés par des virgules.")
delta = b * b - 4 * a * c
if delta > 0 :
    print "Il y a deux solutions."
    print 'Je vous laisse les trouver.'
if delta == 0 :
    print "Il y a une solution unique."
    print "Je ne vous l'indiquerai pas."
if delta < 0 :
    print "Il n'y a aucune solution!"
