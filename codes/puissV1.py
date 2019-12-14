# Puissance récursive version 1
# https://edupython.tuxfamily.org/sources/view.php?code=puissV1

from lycee import *
def puissV1(a,n):
    if n==1 :
        return a                  
    else :
        return a*puissV1(a,n-1)   
print (puissV1(2,10))
