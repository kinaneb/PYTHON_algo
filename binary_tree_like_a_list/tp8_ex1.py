#!/usr/bin/env python3

from tp8 import *
from data import *

#
#
# 

def etiquette(arbre, i) :
  if not estVide(arbre):
    if i < len(arbre):
      return arbre[i][0]
  return None

def filsGauche(arbre, i) :
  if not estVide(arbre):
    if i < len(arbre):
      return arbre[i][1]
  return None


def filsDroit(arbre, i) :
  if not estVide(arbre):
    if i < len(arbre):
      return arbre[i][2]
  return None


#
# A COMPLETER !
#
def estUnABR(arbre) :
  ''' teste si arbre est un ABR '''
  for i in range(len(arbre)):
    if(estFeuille(arbre, i)): continue
    if(not estFeuille(arbre, filsGauche(arbre, i))):
      #print(arbre[i])
      if (etiquette(arbre, i) <= etiquette(arbre, filsGauche(arbre, i)) ):
        return False
    if(not estFeuille(arbre, filsDroit(arbre, i))):
      if (etiquette(arbre, i) > etiquette(arbre, filsDroit(arbre, i)) ):
        return False
  return True

#
# A COMPLETER !
#
def minimumABR(arbre) :
  ''' retourne l'etiquette minimale dans arbre (si c'est un ABR) '''
  if(estUnABR(arbre)):
    if(not estVide(arbre)):
      i = racine(arbre)
      while (not estFeuille(arbre, i)):
        i = filsGauche(arbre, i)
      return pere(arbre, i)
    return None
  return -1
  
#
# A COMPLETER !
#
def maximumABR(arbre) :
  ''' retourne l'etiquette maximale dans arbre (si c'est un ABR) '''
  if(estUnABR(arbre)):
    if(not estVide(arbre)):
      i = racine(arbre)
      while (not estFeuille(arbre, i)):
        i = filsDroit(arbre, i)
      return pere(arbre, i)
    return None
  return 0

#
# A COMPLETER !
#
def rechercheABR(arbre, elt) :
  ''' retourne le noeud contenant elt, ou la feuille ou la recherche
  echoue (si c'est un ABR) '''
  if(not estUnABR(arbre)): return -1
  if(estVide(arbre) ): return 0
  i = racine(arbre)
  if(elt == etiquette(arbre, i) ): return i
  minA = minimumABR(arbre)
  if(elt < etiquette(arbre, minA)): 
    return filsGauche(arbre, minA)
  maxA = maximumABR(arbre)
  if(elt > etiquette(arbre, maxA)): 
    return filsDroit(arbre, maxA)
  while(not estFeuille(arbre, i)):
    if(elt <= etiquette( arbre, i) ):
      i = filsGauche(arbre, i)
      if (elt == etiquette(arbre, i)): return i
    elif(elt > etiquette(arbre, i) ):
      i = filsDroit(arbre, i)
      if(elt == etiquette(arbre, i)): return i
  return i
  
#
# A COMPLETER !
#
def contientABR(arbre, elt) :
  ''' teste is arbre contient elt (si c'est un ABR)'''
  eltIndice = rechercheABR(arbre, elt)
  if(eltIndice != -1):
    if(etiquette(arbre, eltIndice) != None):
      return True
  return False
  
#
# A COMPLETER !
#
def insertionABR(arbre, elt) :
  ''' insere correctement elt dans arbre si arbre ne contient pas encore
  elt (et si c'est un ABR) '''
  eltIndice = rechercheABR(arbre, elt)
  if(eltIndice != -1):
    if(etiquette(arbre, eltIndice) is None):
      arbre.append([None, None, None, eltIndice])
      arbre.append([None, None, None, eltIndice])
      arbre[eltIndice][0] = elt
      arbre[eltIndice][1] = len(arbre)-1
      arbre[eltIndice][2] = len(arbre)-2
      return arbre
  return None

def construireABR(T):
  arbre = [[None, None, None, None]]
  for i in T:
    insertionABR(arbre, i)
  return arbre


#####################################################################
##  TESTS
#####################################################################

def testData():
  return  [ arbreVide, arbre3ABR1, arbre3ABR2, arbre3ABR3, arbre100ABR1, arbre100ABR2]

def testResults():
  return [[minimumABR, 0,[None, 1, 0, 2, 5, 3]],
          [maximumABR, 0, [None, 2, 2, 0, 16, 120]],
          [rechercheABR, 1, [1,27,3,57,100,200],[0,6,2,3,16,156]],
          [contientABR, 1, [1,27,3,57,100,200],[False,False,True,False,True,False]]                   
]

def testAll() :
  tst = testResults()
  arbres = testData()

  print('Arbres : ')
  for j in range(len(arbres)) :
    print(arbres[j])
    dessineArbreBinaire(arbres[j],"./arb_"+str(j))
 
  for i in range(len(tst)) :
    fname = tst[i][0]
    farg = tst[i][1]
    fres = tst[i][2 + farg]
    score = 0
    print('Test %s:' % fname.__name__)
    for j in range(len(arbres)) :
      a = arbres[j]
      print (' - test %d/%d: ' % (j + 1, len(arbres)), end='')
      res = fres[j]
      if (farg == 0) :
        res = fname(a)
      elif (farg == 1) :
        res = fname(a,tst[i][2][j])
      if (res == fres[j]) :
        print(' pass')
        score += 1
      else :
        print(" fail: obtenu ", res, end='')
        print(" <> attendu ", fres[j])
    print ('  score %d/%d ' % (score, len(arbres)))

def testInsertion():
  arbres = [arbreVide, arbre3ABR1, arbre3ABR2, arbre3ABR3, arbre100ABR1, arbre100ABR2]
  elements = [4,4,2,10,27,123]
  res = res_insertion()
  score = 0
  print('Test Insertion')
  for i in range(len(arbres)):
    print (' - test %d/%d: ' % (i + 1, len(arbres)), end='')
    a = copier(arbres[i])
    elt = elements[i]
    insertionABR(a,elt)
    if egalite(a,res[i]):
      print(' pass')
      score += 1
    else:
        print(" fail: obtenu ", print(a), end='')
        print(" <> attendu ", res[i])
  print ('  score %d/%d ' % (score, len(arbres)))
    
if __name__ == '__main__':
  #print(estUnABR(arbre3ABR1))  
  testAll()
  testInsertion()
  T = [5, 3, 7, 2, 4, 6, 8]
  dessineArbreBinaire(construireABR(T))
