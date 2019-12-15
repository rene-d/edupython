# Palindrome1
# http://amienspython.tuxfamily.org/sources/codes/palin1.py

# Créé par IANTE, le 28/12/2010
from __future__ import division
from lycee import *
phrase="kayak"
envers=""
p=len(phrase)-1
while p>=0:
    envers=envers+phrase[p]
    p=p-1
if phrase==envers :
    print phrase,"est un palindrome."
