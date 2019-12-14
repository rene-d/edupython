# Marche aléatoire d'un robot sur une table
# https://edupython.tuxfamily.org/sources/view.php?code=robot

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *

# Un robot est placé au centre d'une table de côté 20.
# On considère le repère centré sur la table,
# les bords de la table sont parallèles aux axes.
# A chaque entier de 1 à 4, on associe un déplacement possible du robot :
# devant, derrière, à gauche ou à droite
# On continue tant que le robot est sur la table
# La variable a est le choix aléatoire de déplacement
# La variable j compte le nombre de déplacements

x, y = 0, 0
j = 0
while x >= -10 and x <= 10 and y >= -10 and y <= 10 :
    a = randint(1,4)
    if a == 1 : x = x + 1
    if a == 2 : y = y + 1
    if a == 3 : x = x - 1
    if a == 4 : y = y - 1
    j = j + 1
print ("le robot est tombé de la table au bout de", j, "secondes.")
