#!/usr/bin/env python3

#importe indirectement tp8, data, et tp8_ex* pour * < 3
from tp8_ex3 import *
from random import randint
from math import *
#
# A COMPLETER !
#
def generer2ABR(per):
    n2 = len(per)
    n = int(sqrt(n2))
    arbre = construireABR(per)
    l = [i+1 for i in range(n2-n)]
    while(l):
        r = randint(0, len(l)-1)
        lr = l[r]
        arbre = suppressionABR(arbre, lr)
        l.remove(lr)
    #print(estUnABR(arbre))
    return arbre

#
# A COMPLETER !
#
def stat2ABR(n,m):
    moy = 0
    for i in range(m):
      arbre = generer2ABR(permutation(n))
      dessineArbreBinaire(arbre)
      moy += hauteur(arbre)
    return moy/m



#
# NE PAS MODIFIER
#
def tracer(limite,pas,m):
    l1 = []
    l2 = []
    for i in range(1,limite,pas):
        l1.append(i)
        print("Calcul pour n = %d"%i)
        l2.append(stat2ABR(i,m))
    plt.plot(l1,l2)
    plt.ylabel('hauteur(n)')
    plt.xlabel('n = nombre noeuds')
    plt.show()
    return ()

if __name__ == '__main__':
    tracer(100,10,10)
