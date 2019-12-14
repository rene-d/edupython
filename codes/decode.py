# décodage affine
# https://edupython.tuxfamily.org/sources/view.php?code=decode

#9uéé%!t!upét|ïQé%!të"
message=""
for i in range(len(texte)):
    lettre=texte[i]
    code=codeAAP(lettre)
    code2=reste(41*code+52,102)
    lettre2=decodeAAP(code2)
    message=message+lettre2
print (message)
