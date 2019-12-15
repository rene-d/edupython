# Multiplication babylonienne
# http://amienspython.tuxfamily.org/sources/codes/babylone.py

from lycee import *

# On veut décomposer le produit de deux nombres en somme de carrés.
# On découpe le rectangle de longueur "Longueur" et de largeur "Largeur"
# en carrés de surfaces maximales.

Longueur = demande ("Premier nombre")
Largeur = demande ("Deuxième nombre")

print Longueur, " x ", Largeur, " = ",         # On fait en sorte que Longueur soit plus grand que Largeur
if Longueur < Largeur :
        Longueur, Largeur = Largeur, Longueur

while Largeur > 0 :                            # Tant que la variable Largeur est supérieure à 0, on répète la boucle
    print Largeur, "² + ",                     # et on complète l'affichage au fur et à mesure sur la même ligne
    Longueur = Longueur - Largeur              # On calcule les dimensions du rectangle restant à remplir
    if Longueur < Largeur :
        Longueur, Largeur = Largeur, Longueur
print 0                                        # Le dernier affichage étant "+" on complète par 0 pour finir l'égalité
