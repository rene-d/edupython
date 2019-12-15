# Puissance récursive version 2
# http://amienspython.tuxfamily.org/sources/codes/puissV2.py

from __future__ import division
from lycee import *
def puissV2(a,n):
    if n==1 :                           # a^1=a
        return a
    elif reste(n,2)==0 :
        temp=puissV2(a,quotient(n,2))   #a^n=(a^(n/2))^2 si n est pair
        return temp*temp
    else :
        return a*puissV2(a,n-1)        #a^n=a*a^(n-1) dans les autres cas

print puissV2(2,10)
