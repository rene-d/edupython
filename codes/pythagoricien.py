# Recherche d'un triplet pythagoricien d'entiers consécutifs
# https://edupython.tuxfamily.org/sources/view.php?code=pythagoricien

# Créé par AgneS, le 17/06/2013 en Python 3.2
for i in range(100000):           # On va tester avec la réciproque de Pythagore
                                  # pour 3 nombres consécutifs compris entre 0 et 100001
    a=i*i+(i+1)*(i+1)      # Le carré de i peut être obtenu aussi en posant i**2 ou puissance(i, 2)
    r=(i+2)*(i+2)
    if r==a:
        print ("les nombres",i,",",i+1,"et",i+2,"forment un triplet pythagoricien")
