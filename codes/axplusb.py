# Solutions de ax+b=0
# https://edupython.tuxfamily.org/sources/view.php?code=axplusb

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *
# Le but de ce programme est de donner la solution de l'équation ax + b = 0
# pour des valeurs de a et b demandées.
# Le programme affiche la solution si elle existe et précise s'il y a unicité.
a=demande("Entrez a de l'équation ax+b=0")
b=demande("Entrez maintenant b de l'équation ax+b=0")
if a!=0:                  # Cas où a est différent de 0:
         # Finir la ligne d'affichage par end="" indique que la ligne n'est
         # pas terminée, il n'y a donc pas de retour à la ligne.
    print ("Il y a une unique solution:",end="")
    print (-b/a)
else:                     # Sinon (c'est-à-dire si a est nul)
    if b==0:              # Sous-cas où b est nul
        print ("Il y a une infinité de solutions.")
        print ("Tous les réels sont solutions.")
    else:
        print ("Il n'y a aucune solution.")
