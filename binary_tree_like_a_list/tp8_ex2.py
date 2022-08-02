#!/usr/bin/env python3

#importe indirectement tp8 et data
from tp8_ex1 import *
from random import randint
import matplotlib.pyplot as plt

# retourne une permutation aleatoire de taille n
# selon la loi de probabilite uniforme
def permutation(n) :
    l = [ (i + 1) for i in range(n) ]
    for i in range(n) :
        r = randint(i, n - 1)
        if i != r :
            l[i], l[r] = l[r], l[i]
    return l

# retourne la hauteur de l'arbre
def hauteur(arbre):
    if estVide(arbre): return 0
    r = racine(arbre)
    return hauteur_aux(arbre,r)

def hauteur_aux(arbre,i):
    if estFeuille(arbre,i): return 0
    h1 = hauteur_aux(arbre,arbre[i][1])
    h2 = hauteur_aux(arbre,arbre[i][2])
    return max(h1,h2) + 1

#
# A COMPLETER !
#
def genererABR(per) :
    # renvoie un ABR construit par insertions successives des elements de la permutation per
    arbre = construireABR(per)
    return arbre
    
#
# A COMPLETER !
#
def statABR(n,m) :
    # renvoie la hauteur moyenne de m arbres de taille n, construit par genereABR  
    moy = 0
    for i in range(m):
        moy += hauteur(genererABR(permutation(n)))
    return moy/m


#
# NE PAS MODIFIER
#
def tracer(limite,pas,m):
    l1 = []
    l2 = []
    for i in range(1,limite,pas):
        l1.append(i)
        l2.append(statABR(i,m))
    plt.plot(l1,l2)
    plt.ylabel('hauteur(n)')
    plt.xlabel('n = nombre noeuds')
    plt.show()
    return ()

#####################################################################
##  TESTS
#####################################################################

def testGenerer():
  arbres = [arbreVide,arbreVide,arbreVide,arbreVide,arbreVide,arbreVide]
  elements = [[2,1,3],[1,2,3],[3,1,2],[1, 2, 4, 3] ,[1, 6, 3, 2, 5, 4], [4, 9, 8, 5, 6, 1, 3, 10, 7, 2]]
  res = res_generer()
#  res = [arbreVide,arbreVide,arbreVide,arbreVide,arbreVide,arbreVide]
  score = 0
  print('Test genereABR')
  for i in range(len(arbres)):
    print (' - test %d/%d: ' % (i + 1, len(arbres)), end='')
    #a = copier(arbres[i])
    elt = elements[i]
    a = genererABR(elt)
    if egalite(a,res[i]):
      print(' pass')
      score += 1
    else:
        print(" fail: obtenu ", print(a), end='')
        print(" <> attendu ", res[i])
  print ('  score %d/%d ' % (score, len(arbres)))
    
if __name__ == '__main__':
    testGenerer()
    tracer(100,10,10)
    pass
