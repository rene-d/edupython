# ???
# https://edupython.tuxfamily.org/sources/view.php?code=suite.liste

# Créé par IANTE, le 14/06/2011
from lycee import *
U=[2,5]
n=1
while n<20 :
    U.append(sqrt(U[n-1]*U[n]+9*(U[n]+1)))
    n=n+1
print (U)
