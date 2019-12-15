# Le pré et la chèvre
# http://amienspython.tuxfamily.org/sources/codes/chevre.py

from __future__ import division
from lycee import *

# Une chèvre broute de l'herbe dans un pré carré de côté 10m.
# Elle est attachée au milieu d'un côté du pré par une corde.
# On cherche à connaître l'aire de la surface d'herbe disponible pour la chèvre
# en fonction de la longueur de la corde.

x = demande ("Longueur de la corde ?")          # Ce programme est basé sur les figures de la documentation situées
                                                # dans le sous paragraphe qui concerne les fonctions Arcsinus et Arccosinus
if x < 5 :
        Aire = pi * x * x / 2
elif x < 10 :
    AngleAEF = acos (5 / x)
    AngleFEG = 180 - 2 * AngleAEF
    Aire = 5 * sqrt (x * x - 5 * 5) + pi * x * x / 360 * AngleFEG
elif x < sqrt (125) :
    AngleMEA = acos (5 / x)
    AngleMEJ = 180 - 2 * AngleMEA
    AngleLEK = 2 * acos (10 / x)
    AngleMEL = 1 / 2 * (AngleMEJ - AngleLEK)
    LK = 2 * x * sin (acos (10 / x))
    Aire = 5 * sqrt (x * x - 5 * 5) + pi * x * x / 180 * AngleMEL + 5 * LK
else :
    Aire = 100                                   # L'aire vaut 100 m² car il s'agit alors du pré entier.
print "L'aire mesure", Aire
