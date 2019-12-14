# PGCD récursif
# https://edupython.tuxfamily.org/sources/view.php?code=pgcdr

# Créé par AgneS, le 20/06/2013 en Python 3.2
from lycee import *
def pgcd_rec(a,b):
    if b==0 :
        return a
    else :
        return pgcd(b,reste(a,b))
print (pgcd_rec(12,28))
