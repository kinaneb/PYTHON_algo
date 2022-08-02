#!/usr/bin/env python3

#importe indirectement tp8, data, et tp8_ex* pour * < 2
from tp8_ex2 import *

#
# A COMPLETER !
#
def maximum2ABR(arbre,i): 
#retourne l'indice du noeud d'etiquette max du sous-arbre enracine en le noeud i
  if(estUnABR(arbre)):
    if(not estVide(arbre) and not estFeuille(arbre, i)):
      while (not estFeuille(arbre, i)):
        i = filsDroit(arbre, i)
      return pere(arbre, i)
    return None
  return -1
  return 0
  
    
#
# A COMPLETER !
#
def relier(arbre, ipere, ifils, d):  
#relier pere et fils. Si d = 1, le fils est un fils gauche et si d = 2, un droit.
  if(d == 1):
    f_g_p = filsGauche(arbre, ipere)
    p_f = pere(arbre, ifils)
    arbre[f_g_p][3] = p_f
    if(estFilsGauche(arbre, ifils)):
      arbre[p_f][1] = f_g_p
    elif(estFilsDroit(arbre, ifils)):
      arbre[p_f][2] = f_g_p
    arbre[ipere][1] = ifils
    arbre[ifils][3] = ipere
  if(d == 2):
    f_d_p = filsDroit(arbre, ipere)
    p_f = pere(arbre, ifils)
    arbre[f_d_p][3] = p_f
    if(estFilsGauche(arbre, ifils)):
      arbre[p_f][1] = f_d_p
    elif(estFilsDroit(arbre, ifils)):
      arbre[p_f][2] = f_d_p
    arbre[ipere][2] = ifils
    arbre[ifils][3] = ipere
  return arbre

def relier_bis(arbre, ipere, ifils, d):  
#relier pere et fils. Si d = 1, le fils est un fils gauche et si d = 2, un droit.
  arbre[ipere][d] = ifils
  arbre[ifils][3] = ipere
  return arbre



#
# A COMPLETER !
#
def suppressionABR(arbre,elt) :
  ''' supprime le noeud d'étiquette elt dans l'arbre '''
  eltI = rechercheABR(arbre, elt)
  if(eltI == -1): return None
  if(etiquette(arbre, eltI) == None): return arbre
  p = pere(arbre, eltI)
  
  if(p != None):
    d = 1 if estFilsGauche(arbre, eltI) else 2
  fg, fd = filsGauche(arbre, eltI), filsDroit(arbre, eltI)
  estFfg, estFfd = estFeuille(arbre, fg), estFeuille(arbre, fd)
  if (p == None and estFfg != estFfd):
    if(not estFfg): f, fs = fg, fd
    else: f, fs = fd, fg
    arbre[f][3] = None 
    suppr(arbre, [eltI, fs])
  elif(estFfg != estFfd and p != None):
    if(not estFfg): f, fs = fg, fd
    else: f, fs = fd, fg
    relier_bis(arbre, p, f, d)
    suppr(arbre, [eltI, fs])
  elif(estFfg and estFfd):
    relier_bis(arbre, p, arbre[eltI][d], d)
    dd = 2 - d + 1
    suppr(arbre, [eltI, arbre[eltI][dd]])
  else:
    pred = maximum2ABR(arbre, fg)
    if(pred != -1):
      arbre[eltI][0] = etiquette(arbre, pred)
      relier_bis(arbre, pere(arbre, pred), filsGauche(arbre, pred),1 if estFilsGauche(arbre, pred) else 2)
      suppr(arbre, [pred, filsDroit(arbre, pred)])
  return arbre
    


#####################################################################
##  TESTS
#####################################################################

def testSuppression():
  arbres = [arbre3ABR1, arbre3ABR1, arbre100ABR1, arbre100ABR1, arbre100ABR1, arbre100ABR1]
  elements = [1,4,1,49,43,55]
  res = res_suppression()
  score = 0
  print('Test Suppression')
  for i in range(len(arbres)):
    print (' - test %d/%d: ' % (i + 1, len(arbres)), end='')
    a = copier(arbres[i])
    elt = elements[i]
    suppressionABR(a,elt)
    if egalite(a,res[i]):
      print(' pass')
      score += 1
    else:
        print(" fail: obtenu ", print(a), end='')
        print(" <> attendu ", res[i])
  print ('  score %d/%d ' % (score, len(arbres)))
    
if __name__ == '__main__':
  T = [[8, 2, 1, None], [10, 10, 9, 0], [2, 4, 3, 0], [7, 6, 5, 2], [1, 20, 19, 2], [None, None, None, 3], [4, 8, 7, 3], [6, 12, 11, 6], [3, 16, 15, 6], [None, None, None, 1], [9, 18, 17, 1], [None, None, None, 7], [5, 14, 13, 7], [None, None, None, 12], [None, None, None, 12], [None, None, None, 8], [None, None, None, 8], [None, None, None, 10], [None, None, None, 10], [None, None, None, 4], [None, None, None, 4]]
  #relier(T, 2, 1, 1)
  #suppressionABR(T, 4)
  #suppressionABR(T, 6)
  #dessineArbreBinaire(T)
  #print(arbre100ABR1[49]) 
  testSuppression()
