#!/usr/bin/env python3

from tp7_ex1_V2 import *

#
# A COMPLETER !
#
def profondeur(arbre, i) :
  ''' retourne la profondeur de i dans l'arbre '''
  if not estVide(arbre):
    if not estRacine(arbre, i):
      p = 1
      rac = False
      while (not rac):
        i = pere(arbre, i)
        p += 1
        if (estRacine(arbre, i)): rac = True
      return i
    return 0  
  return -1
  
#
# NE PAS MODIFIER !
#
def hauteurNaive(arbre) :
  ''' retourne la hauteur de l'arbre '''
  if estVide(arbre) : return 0
  return max (profondeur(arbre, i) for i in range(len(arbre)) 
      if etiquette(arbre, i) != None)
  
#
# A COMPLETER !
#
def hauteur(arbre) :
  ''' retourne la hauteur de l'arbre '''
  return -1
  
#
# A COMPLETER !
#
def parcoursPrefixe(arbre) :
  ''' retourne la liste des etiquettes en ordre prefixe '''
  return None
  
#
# A COMPLETER !
#
def estUnABR(arbre) :
  ''' teste si arbre est un ABR '''
  return False


#
# A COMPLETER !
#

def testResults() :
  return []


#
# NE PAS MODIFIER
#

def testAll() :
  tst = testResults()

  for fname, *tests in tst :
    score = 0
    print('Test %s :' % fname.__name__)
    for j, test in enumerate(tests) :
      *farg, fres = test
      print (' - test %d/%d : ' % (j + 1, len(tests)), end='')
      res = fname(*farg)
      if (res == fres) :
        print(' ok')
        score += 1
      else :
        print(" échec sur", *farg)
        print("\t résultat obtenu :", res, end='')
        print(" <> attendu :", fres)
    print ('  score %d/%d ' % (score, len(tests)))
	
    
if __name__ == '__main__':
  testAll()
