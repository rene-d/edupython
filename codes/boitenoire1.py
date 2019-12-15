# Que fait le programme suivant ?
# http://amienspython.tuxfamily.org/sources/codes/boitenoire1.py

from lycee import *
x = demande ('Entrez une valeur pour x')
y = demande ('Entrez une valeur pour y')
                                             # Notons Xi et Yi les valeurs initiales pour comprendre
x, y = x + y, x - y
                                             # Comme l'affectation est simultanée, les valeurs de x et y pour les deux calculs
                                             # sont ceux de la ligne précédente, Xi et Yi entrées par l'utilisateur.
                                             # On a donc x = Xi + Yi et y = Xi - Yi
x, y = x + y, x - y
                                             # affectation simultanée encore
                                             # x = Xi + Yi + Xi - Yi = 2 Xi et y = Xi + Yi -(Xi - Yi) = 2 Yi
print "maintenant, x=", x, "et y=", y
