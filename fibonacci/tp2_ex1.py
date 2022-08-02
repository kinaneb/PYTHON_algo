#!/usr/bin/env python3

# Pour les fonctions mathematiques
import math

# Pour l'affichage des graphiques
from matplotlib.pyplot import plot, show

# NE PAS MODIFIER
# Calcule
#    le n-eme terme de la suite de Fibonacci 
# par 3 méthodes

def fibo_1(n) :
  if n <= 0 : return 0
  if n <= 2 : return 1
  return fibo_1(n-1) + fibo_1(n-2)

def fibo_2(n) :
  if n <= 0 : return 0
  liste = [0, 1] + [0] * (n-1)
  for i in range(2, n+1) :
    liste[i] = liste[i-1] + liste[i-2]
  return liste[n]

def fibo_3(n) :
  if n <= 0 : return 0
  previous, last = 0, 1
  for i in range(1, n) :
    previous, last = last, previous + last
  return last


###############################################################################
# Exercice 1.1
#
# A REMPLIR
# Calcule
#    le n-eme terme de la suite de Fibonacci et 
#    le nombre d'additions utilisees
  '''oui le numbre d'addition pour (l'utilisation naïve de la récurrence) fibo_1
     est d'order Θ(φ puissance n) 
     mais il est Θ(n) pour (le calcul itératif des n premières valeurs) fibo_2 et fibo_3 '''

# À COMPLÉTER
def fibo_1_adds(n) :
  ops = 0
  if n <= 0 : return 0, ops
  if n <= 2 : return 1, ops
  fb1, op1 = fibo_1_adds(n - 1)
  fb2, op2 = fibo_1_adds(n - 2)
  return fb1 + fb2, op1 + op2 + 1

# À COMPLÉTER
def fibo_2_adds(n) :
  ops = 0
  if n <= 0 : return 0, ops
  liste = [0, 1] + [0] * (n-1)
  for i in range(2, n+1) :
    liste[i] = liste[i-1] + liste[i-2]
    ops += 1
  return liste[n], ops 

# À COMPLÉTER
def fibo_3_adds(n) :
  ops = 0
  if n <= 0 : return 0, ops
  previous, last = 0, 1
  for i in range(1, n) :
    previous, last = last, previous + last
    ops += 1
  return last, ops


###############################################################################
#
# LIRE, NE PAS MODIFIER
#
def colors(tous=True) :
  return ['ro', 'co', 'go', 'bo'] if tous else ['co', 'go', 'bo']

def courbes_adds(n, tous=True, pas=1) :
  ''' affiche les courbes des additions effectuees pour le calcul de Fn par les différents algos
  (les trois si tous=True, valeur par défaut; seulement fibo_2 et fibo_3 si tous=False)'''

  algos = [fibo_1_adds, fibo_2_adds, fibo_3_adds] if tous else [fibo_2_adds, fibo_3_adds] 
  nb_ops = [ [ algo(i)[1] for i in range(0, n, pas) ] for algo in algos ]

  for valeurs, couleur in zip(nb_ops, colors(tous)) :
    plot(range(0,n,pas), valeurs, couleur)
  show()

  
###############################################################################
# Exercice 1.3  
# A REMPLIR
def nbOfBits(i) :
  return int( math.log(i,2) ) + 1 # À COMPLÉTER

  
###############################################################################
# Exercice 1.4
# À COMPLÉTER
def fibo_1_bits(n) :
  ops_bits = 0
  if n <= 0 : return 0, ops_bits
  if n <= 2 : return 1, ops_bits
  fb1, op1 = fibo_1_bits(n - 1)
  fb2, op2 = fibo_1_bits(n - 2)
  #print("1 " , op1, "2 ",op2)
  return fb1 + fb2, (op1 + op2) + nbOfBits(fb1 + fb2)

# À COMPLÉTER
def fibo_2_bits(n) :
  ops_bits = 0
  if n <= 0 : return 0, ops_bits
  liste = [0, 1] + [0] * (n-1)
  for i in range(2, n+1) :
    liste[i] = liste[i-1] + liste[i-2]
    ops_bits += nbOfBits(liste[i])
  return liste[n], ops_bits

# À COMPLÉTER
def fibo_3_bits(n) :
  ops_bits = 0
  if n <= 0 : return 0, ops_bits
  previous, last = 0, 1
  for i in range(1, n) :
    previous, last = last, previous + last
    ops_bits += nbOfBits(last)
  return last, ops_bits                                          


###############################################################################
# Exercice 1.5
# À COMPLÉTER
def courbes_ops(n, tous=True, pas=1) :
  ''' affiche les courbes des opérations élémentaires effectuees pour le calcul de Fn par les différents algos '''

  algos = [fibo_1_bits,fibo_2_bits,fibo_3_bits] if tous else [fibo_2_bits,fibo_3_bits]# À COMPLÉTER
  nb_ops = [ [ algo(i)[1] for i in range(0, n, pas) ] for algo in algos ] # À COMPLÉTER

  for valeurs, couleur in zip(nb_ops, colors(tous)) :
    plot(range(0,n,pas), valeurs, couleur)
  show()



###############################################################################################
###############################################################################################
########################################## TESTS ##############################################
  
#
# NE PAS MODIFIER
#
def test_fibo_1_addsData() :
  return [(0, (0, 0)), (1, (1, 0)), (2, (1, 0)), (3, (2, 1)), (4, (3, 2)), (5, (5, 4)), (6, (8, 7)), (7, (13, 12)), (8, (21, 20)), (9, (34, 33)), (10, (55, 54)), (11, (89, 88)), (12, (144, 143)), (13, (233, 232)), (14, (377, 376)), (15, (610, 609))]

#
# NE PAS MODIFIER
#
def test_fibo_2_addsData() :
  return [(0, (0, 0)), (1, (1, 0)), (2, (1, 1)), (3, (2, 2)), (4, (3, 3)), (5, (5, 4)), (6, (8, 5)), (7, (13, 6)), (8, (21, 7)), (9, (34, 8)), (10, (55, 9)), (11, (89, 10)), (12, (144, 11)), (13, (233, 12)), (14, (377, 13)), (15, (610, 14))]

#
# NE PAS MODIFIER
#
def test_fibo_3_addsData() :
  return [(0, (0, 0)), (1, (1, 0)), (2, (1, 1)), (3, (2, 2)), (4, (3, 3)), (5, (5, 4)), (6, (8, 5)), (7, (13, 6)), (8, (21, 7)), (9, (34, 8)), (10, (55, 9)), (11, (89, 10)), (12, (144, 11)), (13, (233, 12)), (14, (377, 13)), (15, (610, 14))]

#
# NE PAS MODIFIER
#
def test_fibo_addsData(i) :
  if i == 1 : return test_fibo_1_addsData()
  elif i == 2 : return test_fibo_2_addsData()
  else : return test_fibo_3_addsData()

#
# NE PAS MODIFIER
#
def test_fibo_adds(num):
  algos = [fibo_1_adds, fibo_2_adds, fibo_3_adds]
  print('Test %s:' %  algos[num-1].__name__)
  score = 0
  data = test_fibo_addsData(num)
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    Tres, Tops = dt[1]
    fb, ops = algos[num-1](n)
    if (fb == Tres and ops == Tops):
      score += 1
      print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s' % n)
      print('    calcule : ', fb, ',', ops)
      print('    attendu : ', Tres, ', ', Tops)
  print('** Score %d/%d' % (score, ldata))

#
# NE PAS MODIFIER
#
def test_nbOfBitsData() :
  return [[4, 3],
          [7, 3],
          [10, 4],
          [10 ** 2, 7],
          [10 ** 3, 10],
          [10 ** 4, 14]]

#
# NE PAS MODIFIER
#
def test_nbOfBits():
  print('Test nbOfBits:')
  score = 0
  data = test_nbOfBitsData()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    refr = dt[1]
    fb = nbOfBits(n)
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
# NE PAS MODIFIER
#
def test_fibo_1_bits_Data() :
  return [(-1, (0, 0)), (2, (1, 0)), (4, (3, 4)), (8, (21, 52)), (10, (55, 146)), (16, (987, 2760))]

#
# NE PAS MODIFIER
#
def test_fibo_2_bits_Data() :
  return [(-1, (0, 0)), (2, (1, 1)), (4, (3, 5)), (8, (21, 21)), (10, (55, 33)), (16, (987, 85))]

#
# NE PAS MODIFIER
#
def test_fibo_3_bits_Data() :
  return [(-1, (0, 0)), (2, (1, 1)), (4, (3, 5)), (8, (21, 21)), (10, (55, 33)), (16, (987, 85))]

#
# NE PAS MODIFIER
#
def test_fibo_bitsData(i) :
  if i == 1 : return test_fibo_1_bits_Data()
  elif i == 2 : return test_fibo_2_bits_Data()
  else : return test_fibo_3_bits_Data()

#
# NE PAS MODIFIER
#
def test_fibo_bits(num):
  algos = [fibo_1_bits, fibo_2_bits, fibo_3_bits]
  print('Test %s:' %  algos[num-1].__name__)
  score = 0
  data = test_fibo_bitsData(num)
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    Tres, Tops = dt[1]
    fb, ops = algos[num-1](n)
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
  test_fibo_adds(1)
  test_fibo_adds(2)
  test_fibo_adds(3)
  courbes_adds(20)
  courbes_adds(30, tous=False)
  test_nbOfBits()
  test_fibo_bits(1)
  test_fibo_bits(2)
  test_fibo_bits(3)  
  courbes_ops(30)
  courbes_ops(50, tous=False)
