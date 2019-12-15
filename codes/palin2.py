# Palindrome2
# http://amienspython.tuxfamily.org/sources/codes/palin2.py

# Créé par IANTE, le 28/12/2010
from __future__ import division
from lycee import *
phrase="kayak"
envers="";p=0
while p<len(phrase):
    envers=phrase[p]+envers
    p=p+1
if phrase==envers :
    print phrase,"est un palindrome."
