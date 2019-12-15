# Hexadécimal 2
# http://amienspython.tuxfamily.org/sources/codes/hexa2.py

# Créé par IANTE, le 29/12/2010
from __future__ import division
from lycee import *
n=demande("Entrez un nombre inférieur à 255")
alphabet="0123456789ABCDEF"
q=quotient(n,16)
r=reste(n,16)
hexa=alphabet[q]+alphabet[r]
print n,"s'ecrit",hexa,"en base 16"
