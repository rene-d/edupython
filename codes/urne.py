# Une urne de 50 boules
# http://amienspython.tuxfamily.org/sources/codes/urne.py

# Créé par IANTE, le 30/08/2011
from __future__ import division
from lycee import *
Gain=[]
for i in range(10000) :
    Urne=["Blanche"]*30+["Noire"]*20
    B1=choice(Urne)
    Urne.remove(B1)
    B2=choice(Urne)
    Urne.remove(B2)
    B3=choice(Urne)
    if B1==B2 and B2==B3 :
        Gain.append(4)
    else :
        Gain.append(-1)
print "Gain moyen : ",moyenne(Gain)
print "Ecart type : ",ecartype(Gain)
