# ???
# https://edupython.tuxfamily.org/sources/view.php?code=palindrome

# Créé par IANTE, le 09/10/2010
from __future__ import division
from lycee import *
#mot=texte_demande("Entrez un mot")
print (ord("A"))
envers=""
for i in range(len(mot)):
    envers=mot[i]+envers
if mot==envers :
    print ("Le mot",mot,"est un palindrome")
else :
    print ("Le mot",mot,"à l'envers s'écrit",envers,", ce n'est donc pas un palindrome")
print (reversed(mot))
