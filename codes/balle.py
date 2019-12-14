# Chute d'une balle
# https://edupython.tuxfamily.org/sources/view.php?code=balle

from lycee import *
t = np.arange(0, 10, 0.1)
repere.plot(t,50-0.5*0.8*t**2)
repere.title('Hauteur de la balle en fonction du temps')
repere.ylabel("hauteur en mètres")
repere.xlabel("temps en secondes")
repere.text(6,45,r'$h=h_0-\frac{1}{2}gt^2$')
repere.show()
