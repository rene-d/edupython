# ???
# https://edupython.tuxfamily.org/sources/view.php?code=pascal

#initialisation
print ([1])
listeB=listeA
for l in range (2,n+2):
    listeA=listeB[:]
    for i in range (1,l):
        listeB[i]=listeA[i-1]+listeA[i]
    print (listeB)
    listeB.append(0)
