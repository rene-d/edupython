# ???
# https://edupython.tuxfamily.org/sources/view.php?code=LucasLehmer

# Créé par AgneS, le 30/08/2011
from lycee import *
p=demande('entrer p, nombre premier impair')
M=2**p-1
print ("M=2^p  -1=",M)
i,v=2,4

while v!=0 and i<=p:
    i=i+1
    v=v**2-2
    v=v%M
    print ("v(2^", i, ") est congru à", v, "mod M")

if v==0 and i==p:
    print ("Le nombre de Mersenne 2^", p, "-1=", M, "est premier.")
else:
    print ("Le nombre de Mersenne 2^", p, "-1=", M, "n'est pas premier.")
