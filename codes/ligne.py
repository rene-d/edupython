# Ligne de niveau
# https://edupython.tuxfamily.org/sources/view.php?code=ligne

from lycee import *
for i in range(10000):
    x=uniform(-10,10)
    y=uniform(-10,10)
    if x*(6-x)<y*(8+y):
        repere.plot(x,y,'ro')
    else :
        repere.plot(x,y,'go')
repere.show()
