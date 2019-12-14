# Que fait le programme suivant ?
# https://edupython.tuxfamily.org/sources/view.php?code=boitenoire1

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *
x = demande('Entrez une valeur pour x')
y = demande('Entrez une valeur pour y')
                         # Notons Xi et Yi les valeurs initiales pour comprendre
x, y = x + y , x - y     # Comme l'affectation est simultanée, les valeurs de x et y pour les deux calculs
                         # sont celles de la ligne précédente, Xi et Yi entrées par l'utilisateur.
                         # On a donc x = Xi + Yi et y = Xi - Yi

x , y = x + y , x - y    # affectation simultanée encore
                         # x = (Xi + Yi) + (Xi - Yi) = 2 Xi et y = (Xi + Yi) -(Xi - Yi) = 2 Yi
print ("maintenant, x=", x, "et y=", y)
