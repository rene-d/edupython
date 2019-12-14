# codage affine
# https://edupython.tuxfamily.org/sources/view.php?code=code

from lycee import *
texte="Les carottes sont cuites !"
message=""
for i in range(len(texte)):
    lettre=texte[i]
    code=codeAAP(lettre)
    code2=reste(5*code+46,102)
    lettre2=decodeAAP(code2)
    message=message+lettre2
print (message)
