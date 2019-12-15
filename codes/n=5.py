# ???
# http://amienspython.tuxfamily.org/sources/codes/n=5.py

L=[]
for max in range(1,5):
    L.append(puissance(max,5))
max=5
trouve=0
while trouve==0:
    L.append(puissance(max,5))
    ind1=0;
    while ind1<max and trouve==0:
        ind2=ind1
        while ind2<max and trouve==0:
            ind3=ind2
            while ind3<max and trouve==0 :
                ind4=ind3
                while ind4 <max and trouve==0:
                    if L[ind1]+L[ind2]+L[ind3]+L[ind4]==L[max-1]:
                        print ind1+1,"^5+",ind2+1,"^5+",ind3+1,"^5+",ind4+1,"^5=",max,"^5+"
                        print L[ind1],"+",L[ind2],"+",L[ind3],"+",L[ind4],"=",L[max-1]
                        trouve=1
    max=max+1
    print "max=",max
