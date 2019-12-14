# Appel de jugement
# https://edupython.tuxfamily.org/sources/view.php?code=jugement

# Créé par IANTE, le 27/08/2011
from lycee import *
Nb=[]
for i in range(1000):
    Mexicain=0
    for n in range(870):
        if random()<0.791 :
            Mexicain=Mexicain+1
    Nb.append(Mexicain)
baton(Nb)
repere.show()
dec1,dec9=decile(Nb)
print ("80% des valeurs se situent entre",end="")
print (dec1,'et',dec9)
