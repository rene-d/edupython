# La cuve sans fonction
# http://amienspython.tuxfamily.org/sources/codes/cuve1.py

from __future__ import division
from lycee import *

# Une cuve est constituée d'un cône de hauteur 20cm et de rayon 10cm,
# surmonté d'un cylindre de rayon 10cm et de hauteur 20cm.
# On cherche à connaître le volume d'eau contenu dans cette cuve
# en fonction de la hauteur de l'eau.

h = demande ("hauteur d'eau ?")             # On demande la hauteur d'eau

if h < 20 :                                 # Si on est avant la jonction des 2 formes
    R = h / 2                               # On calcule le rayon du cone d'eau à l'aide
    V = 1 / 3 * pi * R * R * h              # du théorème de Thalès
else :
    Vcone = 1 / 3 * pi * 10 * 10 * 20       # Vcone est le volume du cône d'eau
    Vcyl = pi * 10 * 10 * (h - 20)          # Vcyl est le volume du cylindre de hauteur h-20
    V = Vcyl + Vcone                        # On calcule alors le volume total
print "Le volume est", V
