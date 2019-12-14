# Palindrome1
# https://edupython.tuxfamily.org/sources/view.php?code=palin1

# Créé par IANTE, le 28/12/2010
from lycee import *
phrase="kayak"
envers=""
p=len(phrase)-1
while p>=0:
    envers=envers+phrase[p]
    p=p-1
if phrase==envers :
    print (phrase,"est un palindrome.")
