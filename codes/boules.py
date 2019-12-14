# 100 boules
# https://edupython.tuxfamily.org/sources/view.php?code=boules

# Un jeu propose deux règles, on cherche laquelle est la plus avantageuse.
# Une urne contient 100 boules numérotées de 1 à 100.
# On tire deux boules successivement avec remise.
# Règle 1: Le score est l'écart entre les deux numéros tirés.
# Règle 2: Le score est la plus petite des deux valeurs.
# Le but du jeu est d'atteindre le score de 36.
# On effectue 100 000 simulations en vue d'émettre une conjecture
regle1, regle2 = 0, 0

for i in range (100000) :
    boule1 = randint (1, 100)
    boule2 = randint(1, 100)
    if boule1 > boule2 :
            score1 = boule1 - boule2
            score2 = boule2
    else :
            score1 = boule2-boule1
            score2 = boule1
    if score1 == 36 : regle1 = regle1 + 1
    if score2 == 36 : regle2 = regle2 + 1

print ("Avec la règle 1, on a gagné", regle1, "fois sur 100 000.")
print ("Avec la règle 2, on a gagné", regle2, "fois sur 100 000.")
