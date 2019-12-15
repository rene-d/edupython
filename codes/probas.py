# Calcul de probabilités
# http://amienspython.tuxfamily.org/sources/codes/probas.py

from lycee import *
# S étant l'ensemble des multiples de 7
# et T l'ensemble des nombres se terminant par le chiffre 3,
# on compte les éléments de S, T, SnT et SuT parmi les entiers de 1 à 666
# afin de déterminer les probabilités associées.
# On considère chaque nombre entier de 1 à 666 et on teste s'il vérifie
# les conditions d'appartenance pour chaque ensemble :
# si le test est positif alors on ajoute 1 aux cardinaux des ensembles concernés.
p1, p2, p3, p4 = 0, 0, 0, 0
for i in range (1, 667) :
    if reste (i, 7) == 0 : p1 = p1 + 1
    if reste (i, 10) == 3 : p2 = p2 + 1
    if reste (i, 7) == 0 and reste (i, 10) == 3: p3 = p3 + 1    # Intersection
    if reste (i, 7) == 0 or reste (i, 10) == 3 : p4 = p4 + 1    # Réunion
print "p(S) = ", p1, " / 666   p(T) = ", p2, " / 666"
print "p(SnT) = ", p3, " /666   p(SuT) = ", p4, " / 666"
