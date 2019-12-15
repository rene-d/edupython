# ???
# http://amienspython.tuxfamily.org/sources/codes/bissextile.py

# Créé par IANTE, le 04/09/2011
from __future__ import division
from lycee import *
n=demande('année ? ')

if (reste(n,4)==0 and reste(n,100)<>0) or reste(n,400)==0:
    print n,'est une année bissextile'
else :
    print n,"n'est pas une année bissextile"
