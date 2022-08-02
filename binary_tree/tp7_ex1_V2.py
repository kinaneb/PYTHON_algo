#!/usr/bin/env python3

from tp7 import *
from tp7_ex1_test import *

def estVide(arbre) :
  if (arbre == []) or (arbre == [[None, None, None , None]]) :
    return True
  return False

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

  
  
def pere(arbre, i) :
  if not estVide(arbre):
    if i < len(arbre):
      return arbre[i][3]
  return None

  

def estRacine(arbre, i) :
  if not estVide(arbre):
    if i < len(arbre):
      if arbre[i][3] == None : 
        return True
  return False


  
def estFilsGauche(arbre, i) :
  if not estVide(arbre):
    if i < len(arbre):
      if filsGauche(arbre, pere(arbre, i)) == i :
        return True
  return False

  


def estFilsDroit(arbre, i) :
  if not estVide(arbre):
    if i < len(arbre):
      if filsDroit(arbre, pere(arbre, i)) == i :
        return True 
  return False



def estFeuille(arbre, i) :
  if not estVide(arbre):
    if i < len(arbre):
      if (filsGauche(arbre, i) == None) and (filsDroit(arbre, i) == None) and (etiquette(arbre, i) == None) and (not estRacine(arbre, i)) :
        return True 
  return False


    
if __name__ == '__main__':
  testAll()
 # A = [['a', 1, 2, None], [None, None, None, 0], [None, None, None, 0]]
  #print(estFeuille(A,1))
