# Le jeu du nombre mystère
# https://edupython.tuxfamily.org/sources/view.php?code=loto

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *
a=randint(1,100)
n=demande('Proposer une valeur')
if n!=a:   # On teste si l'entier entre 1 et 100 choisi au hasard par la machine
           # est différent du nombre proposé par l'utilisateur
    print ("vous avez perdu, le nombre mystère n'est pas",n)
else:
    print ('gagné, vous devriez jouer au LOTO !')
# L'utilisateur n'a qu'un seul essai pour deviner.
