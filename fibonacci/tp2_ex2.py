#!/usr/bin/env python3

# Pour les tests
import tp2_ex1

# Pour les fonctions mathematiques
import math

# Pour l'affichage des graphiques
from matplotlib.pyplot import plot, show


###############################################################################
# Exercice 2.1
#
# A REMPLIR
#
def produit_matrice_2_2 (M1, M2) :
  '''Effectue le produit de deux matrices 2x2'''
  res = [ [0, 0], [0, 0] ]
  res = [ [( (M1[0][0] * M2[0][0]) + (M1[0][1] * M2[1][0]) ), ( (M1[0][0] * M2[0][1]) + (M1[0][1] * M2[1][1]) )],
          [( (M1[1][0] * M2[0][0]) + (M1[1][1] * M2[1][0]) ), ( (M1[1][0] * M2[0][1]) + (M1[1][1] * M2[1][1]) )] ]
  # A REMPLIR
  return res




###############################################################################
# Exercice 2.2
#
# A REMPLIR 
#
def puissance_matrice_2_2 (M, n) :
  '''Calcule la matrice M a la puissance n par exponentiation rapide'''
  if n == 0 : return [ [1, 0], [0, 1] ] # A REMPLIR
  if n == 1 : return M
  tmp = puissance_matrice_2_2 (M, n//2)
  carre = produit_matrice_2_2 (tmp, tmp)
  return carre if n%2 == 0 else produit_matrice_2_2 (M, carre) # A REMPLIR


#
# NE PAS MODIFIER !!!
#
def fibo_4(n) :
  '''Calcule le n-eme terme de la suite de Fibonacci'''
  if n <= 0 : return 0
  if n <= 2 : return 1
  M = [ [1, 1], [1, 0] ]
  N = puissance_matrice_2_2 (M, n-1)
  return N[0][0]



###############################################################################
# Exercice 2.3
#
# A REMPLIR
#
def produit_matrice_2_2_ops (M1, M2) :
  ''' produit_matrice_2_2 avec calcul du nombre d'operations arithmétiques'''
  res = [ [0, 0], [0, 0] ]
  res = [ [( (M1[0][0] * M2[0][0]) + (M1[0][1] * M2[1][0]) ), ( (M1[0][0] * M2[0][1]) + (M1[0][1] * M2[1][1]) )],
          [( (M1[1][0] * M2[0][0]) + (M1[1][1] * M2[1][0]) ), ( (M1[1][0] * M2[0][1]) + (M1[1][1] * M2[1][1]) )] ]
  # A REMPLIR
  return res, 12 #A REMPLIR

def puissance_matrice_2_2_ops (M, n) :
  ''' puissance_matrice_2_2 avec calcul du nombre d'additions'''
  if n == 0 : return [ [1, 0], [0, 1] ], 0 
  if n == 1 : return M, 0
  tmp, opa = puissance_matrice_2_2_ops (M, n//2) 
  carre, oma = produit_matrice_2_2_ops (tmp, tmp)
  if n%2 == 0 :
    return carre, opa+oma + 1
  else :
    opa += oma
    tmp, oma = produit_matrice_2_2_ops(M, carre)
    return tmp, opa+oma + 1
  # A REMPLIR
  #return M, 0
  
def fibo_4_ops(n) :
  '''fibo_4 avec calcul du nombre d'additions effectuees'''
  if n <= 0 : return 0, 0 
  if n <= 2 : return 1, 0 
  M = [ [1, 1], [1, 0] ]
  # A REMPLIR
  N , oa = puissance_matrice_2_2_ops (M, n-1)
  return N[0][0], oa


###############################################################################
# Exercice 2.4
#
# A REMPLIR
#
def courbes_ops(n, pas=1) :
  ''' affiche les courbes des additions effectuées par fibo_3 et des operations arithmétiques
  effectuées par  fibo_4 '''
  ops = [[]] * 2
  col = tp2_ex1.colors()
  
  # A REMPLIR
  ops[0] = [ tp2_ex1.fibo_3_adds(i)[1] for i in range(0, n, pas) ]
  ops[1] = [ fibo_4_ops(i)[1] for i in range(0, n, pas)] 
  plot(range(0,n,pas), ops[0], col[2])
  plot(range(0,n,pas), ops[1], col[3])
  show()

###############################################################################
# Exercice 2.5
#
# A REMPLIR
#
def produit_matrice_2_2_bits (M1, M2) :
  ''' produit_matrice_2_2 avec calcul du nombre d'operations elementaires'''
  res = [ [0, 0], [0, 0] ]
  res = [ [( (M1[0][0] * M2[0][0]) + (M1[0][1] * M2[1][0]) ), ( (M1[0][0] * M2[0][1]) + (M1[0][1] * M2[1][1]) )],
          [( (M1[1][0] * M2[0][0]) + (M1[1][1] * M2[1][0]) ), ( (M1[1][0] * M2[0][1]) + (M1[1][1] * M2[1][1]) )] ]
  bits = tp2_ex1.nbOfBits(max([res[0][0], res[1][0], res[0][1], res[1][1]]))
  # A REMPLIR
  return res, ( 8 * (bits**2) ) + ( 4 * bits )


def puissance_matrice_2_2_bits (M, n) :
  '''puissance_matrice_2_2 avec calcul du nombre d'operations elementaires'''
  if n == 0 : return [ [1, 0], [0, 1] ], 0 # A REMPLIR
  if n == 1 : return M, 0
  tmp, ope = puissance_matrice_2_2_bits(M, n//2)
  carre, ome = produit_matrice_2_2_bits(tmp, tmp)
  if n%2 == 0 :
    return carre, ope+ome
  else :
    ope += ome
    tmp, ome = produit_matrice_2_2_bits(M, carre)
    return tmp, ope+ome
  return M, 0 # A REMPLIR


def fibo_4_bits(n) :
  '''fibo_4 avec calcul du nombre d'operations elementaires'''
  if n <= 0 : return 0, 0 # A REMPLIR
  if n <= 2 : return 1, 0 # A REMPLIR
  M = [ [1, 1], [1, 0] ]
  M, oe = puissance_matrice_2_2_bits(M, n-1)
  # A REMPLIR
  return M[0][0], oe

###############################################################################
# Exercice 2.4
#
# A REMPLIR
#
def courbes_bits(n, pas=1) :
  ''' affiche les courbes des operations elementaires effectuees pour le calcul de Fn par les algos fibo_3 et fibo_4 '''
  ops = [[]] * 2
  col = tp2_ex1.colors()
  # A REMPLIR
  ops[0] = [ tp2_ex1.fibo_3_bits(i)[1] for i in range(0, n, pas) ]
  ops[1] = [ fibo_4_bits(i)[1] for i in range(0, n, pas) ]
  plot(range(0,n,pas), ops[0], col[2])
  plot(range(0,n,pas), ops[1], col[3])
  show()







  
#####################################################################################
#####################################################################################
################# TESTS #############################################################
#
# NE PAS MODIFIER
#



  

def test_prod22Data() :
  return [ [ [ [3, 0], [5, 6] ], [ [1, 4], [2, 1] ], [ [3, 12 ], [ 17 , 26 ] ] ] ,
           [ [ [20, 16], [ 5, 10 ]  ],  [ [10, 7], [2, 3] ],  [ [232, 188], [70, 65] ] ],
           [ [  [60, 5], [4, 1]  ], [ [54, 30], [11, 4]  ], [ [3295, 1820], [227, 124]] ],
           [ [ [34, 70], [2, 18] ], [ [56, 29], [10, 16] ], [ [2604, 2106], [292, 346]] ],
          [ [ [54, 30], [11, 4] ], [ [60, 5], [4, 1] ] , [ [3360, 300], [676, 59] ] ]
  ]




def test_prod22():
  print('Test produit_matrice_2_2:')
  score = 0
  data = test_prod22Data()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    refr = dt[ 2 ]
    fb = produit_matrice_2_2 ( dt[0], dt[1] )
    if fb == refr :
      score += 1
      print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s' % n)
      print('    calcule : %s' % fb)
      print('    attendu : %s' % refr)
  print('** Score %d/%d' % (score, ldata))




  

def test_puissanceData() :
  return [ [ [ [1, 4], [2, 1] ], 2, [[9, 8], [4, 9]]],
           [ [ [3, 0], [5, 6] ], 3, [[27, 0], [315, 216]] ],
           [ [ [3, 12 ], [ 17 , 26 ] ], 8, [[252018687525, 442324154508], [626625885553, 1099806650332]] ],
           [ [ [20, 16], [ 5, 10 ]  ], 6,  [[192672000, 202176000], [63180000, 66312000]] ],
           [ [ [232, 188], [70, 65] ], 5, [[1640021237352, 1367968885308], [509350116870, 424857387105]] ],
           [ [ [10, 7], [2, 3] ], 4, [[15362, 12467], [3562, 2895]] ],
           [ [  [60, 5], [4, 1]  ], 7 , [[2894868940020, 243934318805], [195147455044, 16443978121]] ],
           [ [ [54, 30], [11, 4]  ], 10, [[538139813380894176, 288789026527531200], [105889309726761440, 56824769168342176]] ],
           [ [ [34, 70], [2, 18] ], 3,  [[51344, 156240], [4464, 15632]] ],
           [ [ [56, 29], [10, 16] ], 2, [[3426, 2088], [720, 546]] ],
           [ [ [54, 30], [11, 4] ], 5 ,  [[697669224, 374399400], [137279780, 73670224]] ],
           [ [ [60, 5], [4, 1] ], 9, [[10538945536660820, 888057647401005], [710446117920804, 59865297328961]] ]
  ]





#
# NE PAS MODIFIER
#
def test_puissance():
  print('Test puissance_matrice_2_2:')
  score = 0
  data = test_puissanceData()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    refr = dt[ 2 ]
    fb = puissance_matrice_2_2 ( dt[0], dt[1] )
    if fb == refr :
      score += 1
      print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s' % n)
      print('    calcule : %s' % fb)
      print('    attendu : %s' % refr)
  print('** Score %d/%d' % (score, ldata))





#
# AJOUTER D'AUTRES DONNEES DE TEST
# [<valeur n>, <valeur F_n>]
def test_fibo_4_opsData() :
  return [(0, (0, 0)), (1, (1, 0)), (2, (1, 0)), (3, (2, 13)), (4, (3, 25)), (5, (5, 26)), (6, (8, 38)), (7, (13, 38)), (8, (21, 50)), (9, (34, 39)), (10, (55, 51)), (11, (89, 51)), (12, (144, 63)), (13, (233, 51)), (14, (377, 63)), (15, (610, 63)), (16, (987, 75)), (17, (1597, 52)), (18, (2584, 64)), (19, (4181, 64))]





#
# NE PAS MODIFIER
#
def test_fibo_4():
  print('Test fibo_4_ops: ')
  score = 0
  data = test_fibo_4_opsData()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    Tres, Tops = dt[1]
    fb, ops = fibo_4_ops(n)
    if (fb == Tres and ops == Tops):
      score += 1
      print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s' % n)
      print('    calcule : ', fb, ', ', ops)
      print('    attendu : ', Tres, ', ', Tops)
  print('** Score %d/%d' % (score, ldata))

  
  


if __name__ == '__main__':
  test_prod22()
  test_puissance()
  test_fibo_4()
  courbes_ops(40,1)
  #courbes_ops(40,1)     
  courbes_bits(40,1)
