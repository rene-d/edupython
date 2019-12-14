# Image d'une fonction définie par morceaux
# https://edupython.tuxfamily.org/sources/view.php?code=Mcomme

# Créé par AgneS, le 17/06/2013 en Python 3.2
#M comme mathématiques
from lycee import *
x=demande('valeur de x')
if x<-4:
    print ('f(',x,')=',8*x+36)
elif x<0: #on est dans le cas où x>=-4 et x<0
    print ('f(',x,')=',-x)
elif x<4: #on est dans le cas où x>=-4 et x>=0 et x<4
    print ('f(',x,')=',x)
else: #on est dans le cas où tous les tests précédents étaient négatifs
    print ('f(',x,')=',-8*x+36)
