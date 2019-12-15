# Tester un codage
# http://amienspython.tuxfamily.org/sources/codes/testcodage.py

# Créé par IANTE, le 29/12/2010
from __future__ import division
from lycee import *
message=""
i=0
for i in range(len(AlphabetAP)):
    lettre=AlphabetAP[i]
    code=codeAAP(lettre)
    code2=reste(51*code*code+46*code+21,102)
    lettre2=decodeAAP(code2)
    message=message+lettre2
doubles=0
for i in range(len(message)):
    if message.count(message[i])>1 :
        doubles=doubles+1
if doubles==0 :
    print "C'est un codage"
else :
    print "Ce n'est pas un codage"
