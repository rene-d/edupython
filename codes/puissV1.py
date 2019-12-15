# Puissance récursive version 1
# http://amienspython.tuxfamily.org/sources/codes/puissV1.py

from __future__ import division
from lycee import *
def puissV1(a,n):
    if n==1 :
        return a                  # a^1=a
    else :
        return a*puissV1(a,n-1)   # Sinon, a^n=a*a^(n-1), et on recommence

print puissV1(2,10)
