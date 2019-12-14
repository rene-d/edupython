# Hexadécimal 1
# https://edupython.tuxfamily.org/sources/view.php?code=hexa1

# Créé par IANTE, le 29/12/2010
from lycee import *
n=demande("Entrez un nombre inférieur à 255")
hexa=""
c=quotient(n,16)
for i in range(2):
    if c<10 : hexa=hexa+str(c)
    elif c==10 : hexa=hexa+"A"
    elif c==11 : hexa=hexa+"B"
    elif c==12 : hexa=hexa+"C"
    elif c==13 : hexa=hexa+"D"
    elif c==14 : hexa=hexa+"E"
    elif c==15 : hexa=hexa+"F"
    c=reste(n,16)
print (n,"s'ecrit",hexa,"en base 16")
