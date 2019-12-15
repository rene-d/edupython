# Avoir une full d'enfants
# http://amienspython.tuxfamily.org/sources/codes/full.py

# Créé par Vinni, le 10/03/2012
from __future__ import division
from lycee import *
freq=[]
n=demande("Nombre de familles dans l'échantillon ?")
for echan in range(1000) :
    nbFull=0
    for partie in range(n) :
        De=listeRandint(0,1,5)
        xi,ni=compte(De,'effectif')
        if ni==[3,2] or ni==[2,3] :
            nbFull=nbFull+1
    freq.append(nbFull/n)
barre(freq)
