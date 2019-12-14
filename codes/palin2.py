# Palindrome2
# https://edupython.tuxfamily.org/sources/view.php?code=palin2

# Créé par IANTE, le 28/12/2010
from lycee import *
phrase="kayak"
envers="";p=0
while p<len(phrase):
    envers=phrase[p]+envers
    p=p+1
if phrase==envers :
    print (phrase,"est un palindrome.")
