# Analyser une fraction
# http://amienspython.tuxfamily.org/sources/codes/parser.py

# Créé par IANTE, le 30/12/2010
from __future__ import division
from lycee import *
frac=texte_demande("Entrez une fraction")
barre=frac.find("/")
if barre==-1 :
    print "Le nombre n'est pas sous forme fractionnaire"
else :
    num=eval(frac[:barre])
    den=eval(frac[barre+1:])
    d=pgcd(num,den)
    num,den=quotient(num,d),quotient(den,d)
    print frac+"="+str(num)+"/"+str(den)
