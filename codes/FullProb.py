# ???
# https://edupython.tuxfamily.org/sources/view.php?code=FullProb

# Créé par Vinni, le 10/03/2012
from __future__ import division
from lycee import *
nbTotal,nbFull=0,0
for d1 in range(2) :
    for d2 in range(2) :
        for d3 in range(2) :
            for d4 in range(2) :
                for d5 in range(2) :
                    nbTotal=nbTotal+1
                    xi,ni=compte([d1,d2,d3,d4,d5],'effectif')
                    if ni==[2,3] or ni==[3,2] :
                        nbFull=nbFull+1
print nbFull,nbTotal,nbFull/nbTotal
