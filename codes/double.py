# Doubler les voyelles
# https://edupython.tuxfamily.org/sources/view.php?code=double

from lycee import *
mot="glouglou dit le dindon"
double=""
i=0;
while i <len(mot):
    if mot[i] in ("a","e","i","o","u","y") :
        double=double+mot[i]*2
    else :
        double=double+mot[i]
    i=i+1
print (double)
