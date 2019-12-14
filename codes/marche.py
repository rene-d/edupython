# Marche aléatoire
# https://edupython.tuxfamily.org/sources/view.php?code=marche

from lycee import *
p,x,y=0,[],[]
for i in range(1000):
    x.append(i)
    y.append(p)
    if randint(0,1)==0:
        p=p+1
    else :
        p=p-1
repere.plot(x,y)
repere.show()
