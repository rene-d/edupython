# Analyser une fraction
# https://edupython.tuxfamily.org/sources/view.php?code=parser

# Créé par IANTE, le 30/12/2010
from lycee import *
frac=input("Entrez une fraction")
barre=frac.find("/")
if barre==-1 :
    print ("Le nombre n'est pas sous forme fractionnaire")
else :
    num=eval(frac[:barre])
    den=eval(frac[barre+1:])
    d=pgcd(num,den)
    num,den=quotient(num,d),quotient(den,d)
    print (frac+"="+str(num)+"/"+str(den))
