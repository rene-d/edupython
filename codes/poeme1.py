# Poème version 1
# https://edupython.tuxfamily.org/sources/view.php?code=poeme1

# Créé par IANTE, le 12/02/2011
from lycee import *

poeme=fich2chaine()
CarSpeciaux=['.',',','!',"'","\n",';','?',':']
for c in CarSpeciaux:
    poeme=poeme.replace(c," ")
mots=poeme.split(" ")
for m in mots:
    if m!="" : print (reste(len(m),10),end="")
