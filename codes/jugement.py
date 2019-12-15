# Appel de jugement
# http://amienspython.tuxfamily.org/sources/codes/jugement.py

# Créé par IANTE, le 27/08/2011
from __future__ import division
from lycee import *
Nb=[]
for i in range(1000):
    Mexicain=0
    for n in range(870):
        if random()<0.791 :
            Mexicain=Mexicain+1
    Nb.append(Mexicain)
baton(Nb)
dec1,dec9=decile(Nb)
print "80% des valeurs se situent entre",
print dec1,'et',dec9
