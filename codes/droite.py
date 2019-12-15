# Tracer d'une droite
# http://amienspython.tuxfamily.org/sources/codes/droite.py

from lycee import *
a,b=demande("Entrez le coefficient directeur et l'ordonnée à l'origine")
x = np.arange(-10, 10, 0.1)
repere.plot(x, a*x+b)
