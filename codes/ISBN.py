# Code ISBN
# http://amienspython.tuxfamily.org/sources/codes/ISBN.py

# Créé par IANTE, le 21/02/2011
from __future__ import division
from lycee import *
code=texte_demande("Entrer le code ISBN sans les - :")
l=len(c)
debut=code[:l-2]       #On peut écrire code[:-1]
fin=code[l-2:]          #On peut écrire code[-1]
total=0
for i in range(9):
    total=total+eval(debut[i])*(10-i)
cle=11-reste(total,11)
if cle==11 : cle=srt(0)
elif cle==10 : cle="X"
else : cle=str(cle)
if cle==fin:
    print "Ce code est valide"
else :
    print "Ce code n'est pas valide"
