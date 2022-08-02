#!/usr/local/bin/python3

#########################################################
# Exercice 1.1
#
# À REMPLIR
#
# Vérifie que T est une permutation
#
def estPerm(T) :
  # À REMPLIR !!
  X = [0]*len(T)
  for i in T:
    if (i<1): return False
    if (i>len(T)): return False
    if (X[i-1]!=0): return False
    X[i-1] = i
  if(X[0]!=1): return False
  return True

###########################################################
# Exercice 1.2
#
# À REMPLIR
#
# Vérifie que T est une permutation
#   et renvoie le nombre de comparaisons et d'affectations effectuées par l'algorithme
#
def estPermOps(T) :
  ops = 0
  # À REMPLIR
  X = [0]*len(T)
  for i in T:
    ops += 1
    if ( i > len(T) ): return False, ops
    ops += 1
    if (i < 1): return False, ops
    ops += 1
    if ( X[i-1] != 0 ): return False, ops
    X[i-1] = i
  ops += 1
  if ( X[0] != 1 ): return False, ops
  ops += len(T)
  return True, ops

##########################################################
# Exercice 1.3
#
# À REMPLIR
#
# Renvoie la permutation inverse de T
#
def inversePerm(T):
  res = [0] * len(T)
  # À COMPLÉTER
  if ( not estPerm(T) ): return None
  for i in range (len(T)):
    res[T[i]-1] = i+1
  return res

##########################################################
# Exercice 1.4
#
# À REMPLIR
#
# Renvoie la permutation inverse de T
#   et le nombre de comparaisons et d'affectations effectuées par l'algorithme
#
def inversePermOps(T):
  res = [0] * len(T)
  ops = 0
  perm, permOp = estPermOps(T)
  ops += permOp + 1
  if( not perm ): return None, ops
  for i in range (len(T)):
    res[T[i]-1] = i+1 
  ops += len(T)
  return res, ops

###########################################################
# Exercice 1.5
#
# À REMPLIR
#
# Calcule la permutation T2 o T1
#
def composePerm(T1, T2):
  res = [0] * len(T1)
  if ( len(T1) != len(T2) ): return None
  if ( not estPerm(T1) ) or ( not estPerm(T2) ): return None
  for (i, e) in enumerate(T1):
    res[i] = T2[e-1]
  # À COMPLÉTER
  return res

#############################################################
# Exercice 1.6
#
# À REMPLIR
#
# Calcule la permutation T2 o T1
#   et renvoie le nombre de comparaisons et d'affectations effectuées par l'algorithme
#
def composePermOps(T1, T2):
  ops = 1
  if ( len(T1) != len(T2) ): return None, ops
  perm1, op1 = estPermOps(T1)
  ops += op1 + 1
  if ( not perm1 ): return None, ops
  perm2, op2 = estPermOps(T2)
  ops += op2 + 1
  if ( not perm2 ): return None, ops
  res = [0] * len(T1)
  ops += len(T1)
  for (i, e) in enumerate(T1):
    res[i] = T2[e-1]
  # À COMPLÉTER
  return res, ops

##############################################################
# TESTS
#

def prettyT(T):
  return str(T) if len(T)<20 else str(T[:20])[:-3]+"...]"

data_testFonction = {}	# dictionnaire {fonction:data}

def testFonction(fonction) :
  print('Test %s :' % fonction.__name__)
  score = 0
  ldata = len(data_testFonction[fonction])
  for i, dt in enumerate(data_testFonction[fonction]):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[:-1]		# tous les elts sauf le dernier
    ref = dt[-1]	# dernier elt
    res = fonction(*T)	# ie fonction(T[0], T[1], ...)
    if res == ref :
      score += 1
      print('ok')
    else :
      print('ÉCHEC')
      print('    entrée  : %s' % prettyT(T))
      print('    résultat obtenu  : %s' % res)
      print('    résultat attendu : %s' % ref)
  print('* Score : %d/%d\n' % (score, ldata))

def testFonctionOps(fonction) :
  print('Test %s :' % fonction.__name__)
  score = 0
  ldata = len(data_testFonction[fonction])
  for i, dt in enumerate(data_testFonction[fonction]):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[:-1]		# tous les elts sauf le dernier
    ref = dt[-1]	# dernier elt
    res = fonction(*T)	# ie fonction(T[0], T[1], ...)
    if res == ref :
      score += 1
      print('ok')
    else :
      print('ÉCHEC')
      print('    entrée  : %s' % prettyT(T))
      print('    résultat obtenu  : %s %d' % res)
      print('    résultat attendu : %s %d' % ref)
  print('* Score : %d/%d\n' % (score, ldata))


##############################################################
#
# Tests : estPerm
#

data_testFonction[estPerm] = [
  [[4,3,1], False],
  [[1,2,3,1], False],
  [[1,2,5,3], False],
  [[4,2,1,3], True],
  [[5, 4, 3, 2, 1], True],
  [[3, 1, 2, 4, 5], True],
  [[1, 2], True],
  [[2, 1], True],
  [[3, 1, 4, 2], True],
  [[2, 3, 1, 4], True],
  [[3, 2, 1], True],
  [[2, 3, 1], True]
  ]

##############################################################
#
# Tests : estPermOps
#

data_testFonction[estPermOps] = [
  [[3,2,1], (True, 15)],
  [[4,2,1,3], (True, 20)],
  [[3,2,3,4], (False, 15)],
  [[5,3,2,1,4], (True, 25)],
  [[4,2,1], (False, 1)]
  ]


##############################################################
#
# Tests : inversePerm
#

data_testFonction[inversePerm] = [
  [[3,1,2,4], [2,3,1,4]],
  [[1,4,3,2], [1,4,3,2]],
  [[1,2,3,4], [1,2,3,4]],
  [[2,3,4,1], [4,1,2,3]],
  [[2,3,4,3], None],
  [[2,3,4], None],
  [[4,2,1], None],
  [[5, 4, 3, 2, 1], [5,4,3,2,1]],
  [[3, 1, 2, 4, 5], [2,3,1,4,5]],
  [[1, 2], [1,2]],
  [[2, 1], [2,1]],
  [[3, 1, 4, 2], [2,4,1,3]],
  [[2, 3, 1, 4], [3,1,2,4]],
  [[3, 2, 1], [3,2,1]],
  [[2, 3, 1], [3,1,2]]
  ]

##############################################################
#
# Tests : inversePermOps
#

data_testFonction[inversePermOps] = [
  [[3,1,2,4], ([2,3,1,4], 24)],
  [[3,2,4,5], (None, 20)],
  [[5,2,4,1,3], ([4,2,5,3,1], 30)]
  ]

##############################################################
#
# Tests : composePerm
#

data_testFonction[composePerm] = [
  [[4,3,2,1], [4,3,2,1], [1,2,3,4]],
  [[1,4,3,2], [1,4,3,2], [1,2,3,4]],
  [[1,4,3,2], [4,3,1,2], [4,2,1,3]],
  [[4,3,2,3], [4,3,2,1], None],
  [[1,4,3,2], [1,4,2,2], None],
  [[1,4,3], [4,3,1,2], None],
  [[1,3,2], [1,4,2,3], None],
  [[5, 4, 3, 2, 1], [5,4,3,2,1], [1,2,3,4,5]],
  [[3, 1, 2, 4, 5], [2,3,1,4,5], [1,2,3,4,5]],
  [[1, 2], [1,2], [1,2]],
  [[2, 1], [2,1], [1,2]],
  [[3, 1, 4, 2], [2,4,1,3], [1,2,3,4]],
  [[2, 3, 1, 4], [3,1,2,4], [1,2,3,4]],
  [[3, 2, 1], [3,2,1], [1,2,3]],
  [[2, 3, 1], [3,1,2], [1,2,3]]
  ]

##############################################################
#
# Tests : composePermOps
#

data_testFonction[composePermOps] = [
 [[4,3,2,1], [4,3,2,1], ([1,2,3,4], 49)], 
 [[4,2,1], [3,1,2], (None, 1)],
 [[3,2,1], [2,3,1], ([1,3,2], 37)],
 [[3,2,5,1,4], [4,3,5,2,1], ([5,3,1,4,2], 61)]
 ]

##############################################################

if __name__ == '__main__':
  for fonction in [ estPerm, inversePerm, composePerm] :
    testFonction(fonction)
  for fonction in [ estPermOps, inversePermOps, composePermOps ] :
    testFonctionOps(fonction)
