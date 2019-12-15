# Un tirage de LOTO
# http://amienspython.tuxfamily.org/sources/codes/loto1.py

from __future__ import division
from lycee import *
boules=range(1,50)
for i in range(5):
    b=choice(boules)
    print "boule",i+1,":",b
    boules.remove(b)
print "Numéro chance :",randint(1,10)
