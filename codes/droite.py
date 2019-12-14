# Tracer une droite
# https://edupython.tuxfamily.org/sources/view.php?code=droite

from lycee import *
a,b=demande("Entrez le coefficient directeur et l'ordonnée à l'origine")
x = np.arange(-10, 10, 0.1)
repere.plot(x, a*x+b)
repere.show()
