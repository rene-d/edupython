# décodage affine
# http://amienspython.tuxfamily.org/sources/codes/decode.py

from __future__ import division
from lycee import *
texte="D%!t|#9uéé%!t!upét|ïQé%!të"
message=""
for i in range(len(texte)):
    lettre=texte[i]
    code=codeAAP(lettre)
    code2=reste(41*code+52,102)
    lettre2=decodeAAP(code2)
    message=message+lettre2
print message
