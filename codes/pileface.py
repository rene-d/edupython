# Pile ou facesssss
# http://amienspython.tuxfamily.org/sources/codes/pileface.py

from __future__ import division
from lycee import *
p,f,e=0,0,0
n,ecart,ecartm,freqP,freqF=[],[],[],[],[]
for i in range(1,1000):
    if randint(0,1)==0:
        p=p+1
    else :
        f=f+1
    e=p-f;
    n.append(i)
    ecart.append(e)
    ecartm.append(e/i)
    freqP.append(p/i)
    freqF.append(f/i)
repere.subplot(221)
repere.plot(n,ecart)
repere.title(u"écarts en nombre")
repere.subplot(222)
repere.plot(n,ecartm)
repere.title(u"écarts en fréquence")
repere.subplot(223)
repere.plot(n,freqP)
repere.title(u"% de piles obtenus")
repere.subplot(224)
repere.plot(n,freqF)
repere.title(u"% de faces obtenus")
repere.show();
