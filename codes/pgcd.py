# Calcul du PGCD de 2 entiers strictement positifs
# https://edupython.tuxfamily.org/sources/view.php?code=pgcd

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *

# On utilise l'algorithme d'Euclide pour déterminer le PGCD de a et b.

a,b = demande("Entrez deux entiers strictement positifs.")
                # L'utilisateur doit saisir les nombres séparés par une virgule
print ("PGCD (",a,",",b,") = ", end="")
while b != 0 :                 # La condition de poursuite de la boucle :
                               # tant que le reste de la division n'est pas nul.
    a, b = b, reste(a,b)
print (a)
