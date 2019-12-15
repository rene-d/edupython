# Le jeu du nombre mystère
# http://amienspython.tuxfamily.org/sources/codes/loto.py

from __future__ import division
from lycee import *
a = randint (1, 100)
n = demande ('Proposer une valeur')
if n <> a :  # On teste si l'entier entre 1 et 100 choisi au hasard par la machine
             # est différent du nombre proposé par l'utilisateur
    print "Vous avez perdu, le nombre mystère n'est pas", n
else :
    print 'Gagné, vous devriez jouer au LOTO !'
             # L'utilisateur n'a qu'un seul essai pour deviner.
