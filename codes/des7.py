# Obtenir 7
# https://edupython.tuxfamily.org/sources/view.php?code=des7

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *

# On cherche à connaître la fréquence du résultat 7 pour la somme
# lorsqu'on lance deux dés à 6 faces 100 000 fois chacun.
# j compte le nombre de 7 donc j / 100 000 est la fréquence cherchée

j = 0
for i in range (100000):            # Pour 100 000 lancers de 2 dés.
                                    # Une alternative consisterait en la demande
                                    # du nombre de lancers de dés.
    s = randint(1,6) + randint(1,6)
    if s == 7 :
        j = j+1
f = j / 100000                      # Pas d'espace pour séparer les milliers
print ("le 7 est sorti", j,"fois donc avec une fréquence égale à",f)
