# Comparaison de deux départements
# http://amienspython.tuxfamily.org/sources/codes/population.py

# Créé par IANTE, le 04/09/2011
from __future__ import division
from lycee import *
etendue=1000
nbclasse=quotient(140000,etendue)
#Lecture de la colonne C : Somme
L=CSV2liste('C')
Pop80=[0]*nbclasse
for v in L :
    classe=quotient(v,etendue)
    Pop80[classe]=Pop80[classe]+1
#Lecture de la colonne F : Seine saint-denis
L=CSV2liste('F')
Pop93=[0]*nbclasse
for v in L :
    classe=quotient(v,etendue)
    Pop93[classe]=Pop93[classe]+1
Pop=[i*etendue for i in range(nbclasse+1)]
polygoneFCC(Pop,Pop80,'b')
polygoneFCC(Pop,Pop93,'r')
repere.title('Population dans le 80 et le 93')
repere.ylabel('Fréquences')
repere.xlabel("Nombre d'habitants")
