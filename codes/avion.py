# surréservation
# https://edupython.tuxfamily.org/sources/view.php?code=avion

# Dans un aéroport, un avion peut contenir 100 personnes et la compagnie vend
# 107 réservations.
# Un passager ayant réservé sa place à une chance sur 10
# de ne pas avoir de places dans l'avion.
# Le programme permet de simuler aléatoirement le pourcentage de risque sur 10000
# vols qu'un passager n'ait pas de place dans l'avion et doive embarquer dans
# le vol suivant:

# La variable surbook est initialisée à 0.
surbook=0

# Début de la boucle: La variable simul prend les valeurs entières de 0 à 9999.
for simul in range(10000):
    # Pour chaque valeur de simul, P est une liste de 107 nombres générés
    # aléatoirement compris entre 0 et 9.
    P=listeRandint(0,9,107)
    # venus compte le nombre d'éléments de P différents de 0.
    venus=107-P.count(0)
    if venus>100 :
        # Surbook compte le nombre de vols n'ayant pas pu embarquer tous les
        # passagers munis d'un billet.
        surbook=surbook+1
    # Fin de la boucle For
# Affichage du pourcentage de vols surbookés.
print ("Dans",surbook/100,"% des vols certaines personnes n'ont pu embarquer")
