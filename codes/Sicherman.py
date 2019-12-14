# Dés de Sicherman
# https://edupython.tuxfamily.org/sources/view.php?code=Sicherman

# Créé par IANTE, le 29/07/2011
from lycee import *
De1=[1,2,2,3,3,4]
De2=[1,3,4,5,6,8]
L1=[];L2=[]
for i in range(10000):
    L1.append(randint(1,6)+randint(1,6))
    L2.append(De1[randint(0,5)]+De2[randint(0,5)])
X,F=compte(L1,'frequence')
repere.plot(X,F,'bo')
X,F=compte(L2,'frequence')
repere.plot(X,F,'rx')
repere.show()
