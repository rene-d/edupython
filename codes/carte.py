# Codes de carte bleue
# http://amienspython.tuxfamily.org/sources/codes/carte.py

# Créé par IANTE, le 27/08/2011
from __future__ import division
from lycee import *
ListeMeme=[]
for i in range(10000):
    Carte1=listeRandint(0,9,4)
    Carte2=listeRandint(0,9,4)
    meme=0
    for touche in range(10):
        if touche in Carte1 and touche in Carte2 :
            meme=meme+1
    ListeMeme.append(meme)
print "En moyenne, on a",moyenne(ListeMeme),"touches en commun"
baton(ListeMeme)
