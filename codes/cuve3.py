# ???
# https://edupython.tuxfamily.org/sources/view.php?code=cuve3

# Créé par IANTE, le 17/07/2011
from __future__ import division
from lycee import *
def V(h):
    if h<20 :
        R=h/2
        return 1/3*pi*R*R*h
    else :
        Vcyl=1/3*pi*10*10*20
        Vcone=pi*10*10*(h-20)
        return Vcyl+Vcone

X=range(41)
Y=[]
for x in X : Y.append(V(x))
repere.plot(X,Y)
repere.show()
