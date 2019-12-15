# Suite
# http://amienspython.tuxfamily.org/sources/codes/suite.py

from __future__ import division
from lycee import *
U=[2]
n=1
while n<20 :
    k=1
    total=0
    while k<=n :
        total=total+puissance(-1,k+1)*k*U[n-k]
        k=k+1
    U.append(total)
    n=n+1
print U
