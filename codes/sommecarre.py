# Somme des carrés des 100 premiers entiers
# http://amienspython.tuxfamily.org/sources/codes/sommecarre.py

from __future__ import division
from lycee import *
# On calcule la somme 1² + 2² + 3² + ... + 100²
total = 0
for n in range (1, 101) :   # n prend toutes les valeurs entières de 1 à 100
    total = total + n * n
    if n < 100 :            # Test afin d'adapter l'affichage à la valeur de n
                            # dans une boucle dont on connaît le nombre de répétitions.
        print n, "² + ",
    else :
        print n, "² = ",
print total
