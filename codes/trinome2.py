# signe d'un trinôme
# https://edupython.tuxfamily.org/sources/view.php?code=trinome2

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *
a,b,c=demande("Entrez les coefficients du trinôme séparés par des virgules.")
delta=b*b-4*a*c
if delta<0:
    if a>0:
        print ("P(x)>0 pour tout réel x")
    if a<0:
        print ("P(x)<0 pour tout réel x")
if delta==0:
    if a>0:
        print ("P(x) est positif pour tout réel x")
    if a<0:
        print ("P(x)est négatif pour tout réel x")
if delta>0:
    if a>0:
        print ("P(x)>0 à l'extérieur des racines")
    if a<0:
        print ("P(x)<0 à l'extérieur des racines")
