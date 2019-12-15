# ???
# http://amienspython.tuxfamily.org/sources/codes/pascal.py

from __future__ import division
from lycee import *
n=demande('quelle puissance ?')
listeA=[1,0] #initialisation
print [1]
listeB=listeA
for l in range (2,n+2):
    listeA=listeB[:]
    for i in range (1,l):
        listeB[i]=listeA[i-1]+listeA[i]
    print listeB
    listeB.append(0)
