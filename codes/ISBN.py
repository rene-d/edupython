# Code ISBN
# https://edupython.tuxfamily.org/sources/view.php?code=ISBN

# Créé par IANTE, le 21/02/2011
from lycee import *
code=input("Entrer le code ISBN sans les - :")
l=len(code)
debut=code[:l-1]       #On peut écrire code[:-1]
fin=code[l-1:]          #On peut écrire code[-1]
total=0
for i in range(l-1):
    total=total+eval(debut[i])*(10-i)
cle=11-reste(total,11)
if cle==11 : cle=str(0)
elif cle==10 : cle="X"
else : cle=str(cle)
if cle==fin:
    print ("Ce code est valide")
else :
    print ("Ce code n'est pas valide")
