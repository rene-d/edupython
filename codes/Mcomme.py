# Image d'une fonction définie par morceaux
# http://amienspython.tuxfamily.org/sources/codes/Mcomme.py

# M comme mathématiques
from lycee import *
x = demande ('valeur de x')
if x < -4 :
    print 'f(', x, ') =', 8 * x + 36
elif x < 0 :                                 # On est dans le cas où x >= -4 et x < 0
    print 'f(', x, ') =', -x
elif x < 4 :                                 # On est dans le cas où x >= -4 et x >= 0 et x < 4
    print 'f(', x, ') =', x
else:                                        # On est dans le cas où tous les tests précédents étaient négatifs
    print 'f(', x, ') =', -8 * x + 36
