# Approximation historique du nombre pi
# http://amienspython.tuxfamily.org/sources/codes/approx.py

from __future__ import division
from lycee import *

# On cherche une fraction n/d qui approxime pi mieux que 22/7
# Le numérateur n et le dénominateur d
# sont des entiers positifs non nuls strictement inférieurs à 100
# La nouvelle erreur e, écart entre pi et n/d
# doit être inférieure à l'erreur historique err calculée ci-dessous

err = 22 / 7 - pi
print "erreur historique :", err
for d in range(1,100) :
    # Début de la boucle for
    # La variable d prend les valeurs entières de 1(inclus) à 99
    for n in range(3*d, 4*d) :
        # Comme 3 < pi < 4, n doit être dans l'intervalle [3d;4d[
        f = n / d          # La variable f prend la valeur de la fraction testée
        # Pour estimer l'erreur, on calcule l'écart entre f et pi
        # en commencant par le plus grand pour que l'erreur soit positive
        if f < pi :
            e = pi - f
        else :
            e = f - pi
        # Si l'erreur e obtenue est inférieure à la précédente erreur,
        # e devient la nouvelle erreur à réduire,
        # qui remplace la précédente valeur de err
        if e < err :
            err = e
            # On affiche alors sur la même ligne (car virgule en fin de ligne)
            # la fraction et la nouvelle marge d'erreur à réduire
            print "J'ai trouvé mieux :", n, "/", d, ". ",
            print "L'erreur est :", err
