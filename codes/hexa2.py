# Hexadécimal 2
# https://edupython.tuxfamily.org/sources/view.php?code=hexa2

# Créé par IANTE, le 29/12/2010
from lycee import *
n=demande("Entrez un nombre inférieur à 255")
alphabet="0123456789ABCDEF"
q=quotient(n,16)
r=reste(n,16)
hexa=alphabet[q]+alphabet[r]
print (n,"s'ecrit",hexa,"en base 16")
