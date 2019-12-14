# Calculer l'IMC
# https://edupython.tuxfamily.org/sources/view.php?code=IMC

# Créé par AgneS, le 17/06/2013 en Python 3.2
from lycee import *
m=demande("masse en kilo : ")
t=demande("taille en mètre : ")
IMC=m/(t*t)
print ("L'IMC est de : ",IMC)
