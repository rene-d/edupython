# nombre de 6 obtenus en lançant un dé 10 fois
# https://edupython.tuxfamily.org/sources/view.php?code=nb6

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *

# On compte le nombre de 6 lors de 10 lancers de dé.

nb6=0                          # La variable nb6 est le compteur des 6 obtenus.
                               # On l'initialise à la valeur 0 avant la boucle.
for i in range(10):            # On effectue cette boucle 10 fois.
    if randint(1,6)==6:
        nb6=nb6+1          # On ne stocke pas la valeur du dé dans une variable.
                           # On teste seulement si cette valeur aléatoire (entier entre 1 et 6) vaut 6.
                           # Dans ce cas, on augmente le compteur d'une unité.
print ("Sur les 10 lancers, on a obtenu", nb6, 'fois le numéro "6".')
