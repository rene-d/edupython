# Nombre de Kaprekar
# http://amienspython.tuxfamily.org/sources/codes/nombre.kaprekar.py

# Créé par IANTE, le 20/06/2011
from __future__ import division
from lycee import *
n=demande("Entrez un nombre entier strictement positif")
N=n*n
L=[]
trouveG,trouveD=-1,-1
while N<>0 :
    L.insert(0,reste(N,10))
    N=quotient(N,10)
for i in range(len(L)) :
    gauche=0
    droite=0
    for j in range(i) :
        gauche=gauche*10+L[j]
    for j in range(i,len(L)) :
        droite=droite*10+L[j]
    if gauche+droite==n :
        trouveG,trouveD=gauche,droite
if trouveG>-1:
    print n,"est nombre de Kaprekar",
    print n,"²=",n*n," et ",n,"=",trouveG,"+",trouveD
else :
    print n,"n'est pas nombre de Kaprekar"
