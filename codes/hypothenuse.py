# Calcul de la longueur de l'hypoténuse dans triangle rectangle
# http://amienspython.tuxfamily.org/sources/codes/hypothenuse.py

from lycee import *
a,b=demande("Entrer les longueurs des deux côtés les plus courts du triangle rectangle séparés par une virgule")
h=sqrt(a*a+b*b)
print "L'hypoténuse mesure",h
