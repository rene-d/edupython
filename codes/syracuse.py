# Suite de Syracuse
# https://edupython.tuxfamily.org/sources/view.php?code=syracuse

# La fonction qui retourne le nombre qui vient
    if reste(x,2)==0:       # après x dans la suite de Syracuse
        return quotient(x,2)
    else :
        return 3*x+1

def vol(x):                 # Fonction qui renvoie une liste contenant
    L=[]                    # toutes les valeurs de la suite de Syracuse
    while x!=1 :            # en partant de x.
        L.append(x)
        x=suivant(x)        # Cette fonction appelle à son tour la fonction "suivant"
    return L

tmax=0
for n in range(1,100001):
    t=len(vol(n))
    if t>tmax :
        print ("Temps de vol de",t,"pour n=",n)
        tmax=t
