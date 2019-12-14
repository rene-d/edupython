# Un tirage de LOTO
# https://edupython.tuxfamily.org/sources/view.php?code=loto1

from lycee import *
boules=list(range(1,50))
for i in range(5):
    b=choice(boules)
    print ("boule",i+1,":",b)
    boules.remove(b)
print ("Numéro chance :",randint(1,10))
