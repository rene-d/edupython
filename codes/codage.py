# ???
# http://amienspython.tuxfamily.org/sources/codes/codage.py

# Créé par IANTE, le 29/12/2010
from __future__ import division
from lycee import *
texte="Les carottes sont cuites !"
message=""
for i in range(len(texte)):
    lettre=texte[i]
    code=codeAAP(lettre)
    code2=reste(5*code+46,102)
    lettre2=decodeAAP(code2)
    message=message+lettre2
print message
