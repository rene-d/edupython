# ???
# https://edupython.tuxfamily.org/sources/view.php?code=suite.sans.liste

# Créé par IANTE, le 14/06/2011
from lycee import *
a,b,n=2,5,1
while n<=20 :
    print (a," ", end="")
    a,b=b,sqrt(a*b+9*(b+1))
    n=n+1
