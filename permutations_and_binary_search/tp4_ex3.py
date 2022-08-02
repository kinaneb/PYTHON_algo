#!/usr/local/bin/python3

#
# NB: T est toujours considéré trié !
#
from tp4_ex2 import occurrenceOps
############################################################
# Exercice 2.1
#
# Effectue une recherche dichotomique de x dans T
#

def trouve(T, x):
  # A REMPLIR/MODIFIER !!
  if (len(T) == 0): return False
  m = len(T)//2
  if (x == T[m]): return True
  elif (x < T[m]): return trouve(T[:m],x)
  return trouve(T[m+1:],x)
  



############################################################
# Exercice 2.2
#
# Effectue une recherche dichotomique de x dans T
# et le nombre de comparaisons effectees

def trouveOps(T,x):
  # A REMPLIR/MODIFIER !!
  if (len(T) == 0): return False, 1
  m = len(T)//2
  if (x == T[m]): return True,2
  elif (x < T[m]): 
    ops = 3
    trouve, op = trouveOps(T[:m],x)
    ops += op
    return trouve, ops
  else: 
    ops = 3
    trouve, op = trouveOps(T[m+1:],x)
    ops += op
    return trouve, ops



############################################################
# Exercice 2.3
#
# Renvoie l'indice de la première occurrence de x dans T
# et False si il n'y en a aucune
#
# Aide: vous pouvez utiliser l'argument optionnel 'debut'
#   plutôt que de définir une fonction auxiliaire
#

def trouvePremier(T, x,debut=0) :
  # A REMPLIR/MODIFIER !!
  if (len(T) == 0):return False
  m = len(T)//2
  debut += m
  if (x == T[m]):
    if not trouve(T[:m],x):return debut
    else: return trouvePremier(T[:m],x,debut - m)
  elif (x < T[m]):
    if not trouve(T[:m], x): return False
    else: return trouvePremier(T[:m],x,debut - m)
  else:
    if not trouve(T[m:], x): return False
    else: return trouvePremier(T[m:],x,debut)
  

############################################################
# Exercice 2.4
#
# Renvoie l'indice de la première occurrence de x dans T
# et False si il n'y en a aucune
# ainsi que le nombre de comparaisons nécessaires
#
  

def trouvePremierOps(T, x, debut=0) :
  # À remplir
  if (len(T) == 0):return False,1
  m = len(T)//2
  debut += m
  if (x == T[m]):
    ops = 2
    #trouve, op = trouveOps(T[:m],x) ilfaut qu'on utilise cette fonction et il faut qu'on ajout op a ops    mais ça crée des echec
    ops += 1
    if not (trouve(T[:m],x)) :return debut, ops
    else:
      trouveP, opP = trouvePremierOps(T[:m],x,debut - m)
      ops += opP 
      return trouveP, ops
  elif (x < T[m]):
    ops = 3
    #trouve , op = trouveOps(T[:m],x)
    ops += 1
    if not trouve(T[:m],x): return False, ops
    else:
      trouveP, opP = trouvePremierOps(T[:m],x, debut - m)
      ops += opP 
      return trouveP, ops
  else:
    ops = 3
    #trouve, op = trouveOps(T[m:],x)
    ops += 1
    if not trouve(T[m:],x): return False, ops
    else: 
      trouveP, opP = trouvePremierOps(T[m:],x,debut)
      ops += opP
      return trouveP, ops
  



############################################################
# Exercice 2.5
#
# Compte les occurrences de x dans T par recherche dichotomique
#

#
# une fonction auxiliaire qui renvoi l'indice de la dernier occurrence
#
def trouveDer(T, x,debut=0) :
    if (len(T) == 0):return False
    m = len(T)//2
    debut += m
    #print(m)
    if (x == T[m]):
        if not trouve(T[m+1:],x):return debut
        else: return trouveDer(T[m:],x,debut)
    elif(x > T[m]):
        if not trouve(T[m:], x): return False
        else: return trouveDer(T[m:],x,debut)
    elif (x < T[m]):
        if not trouve(T[:m], x): return False
        else: return trouveDer(T[:m],x,debut-m)

def occurrenceDichotomie(T, x) :
  # A REMPLIR !!
  prem = trouvePremier(T,x)
  der = trouveDer(T,x)
  #print("\nd ", der, "  p ",prem)
  if (prem is False): return 0
  return 1 + der - prem

############################################################
# Exercice 2.5
#
# Compte les occurrences de x dans T par recherche dichotomique
#     et le nombre d'opérations
#
def trouveDerOps(T, x,debut=0) :
    if (len(T) == 0):return False ,1
    m = len(T)//2
    debut += m
    if (x == T[m]):
        ops = 2
        if not trouve(T[m+1:],x):return debut, ops
        else:
            trouveD ,op = trouveDerOps(T[m:],x,debut)
            ops += op
            return trouveD, ops
    elif(x > T[m]):
        ops = 3
        if not trouve(T[m:], x): return False, ops
        else: 
            trouveD ,op = trouveDerOps(T[m:],x,debut)
            ops += op
            return trouveD, ops
    else:
        ops = 3
        if not trouve(T[:m], x): return False, ops
        else: 
            trouveD ,op = trouveDerOps(T[:m],x,debut-m)
            ops += op
            return trouveD, ops


def occurrenceDichotomieOps(T, x) :
  # A REMPLIR !!
  prem, opP = trouvePremierOps(T,x)
  der, opD  = trouveDerOps(T,x)
  if (prem is False): return 0, opP  + opD + 1
  return 1 + der - prem, opP + opD 




############################################################
# TESTS - À COMPLETER 
#

def test_comparOccurrenceOps() :
  print('Test comparOccurrenceOps:')
  data = occurrenceDichotomieOpsData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    T = dt[0]
    x = dt[1]
    opsdata = dt[2]
    resD, opsD = occurrenceDichotomieOps(T,x)
    resO, opsO = occurrenceOps(T,x)
    print("\n		occurrenceDichotomieOps: ",opsD, "\n		occurrenceOps:           ",opsO)
 



def prettyT(T):
  return str(T) if len(T)<20 else str(T[:20])[:-3]+"...]"


############################################################
#
# Tests :
#


def test_trouveData() :
  return [[[1,2,3,4], 2, True],
          [[1,2,4,5] , 3, False],
          [[1,3,5,7,9], 5, True],
          [[1,3,5,7,9], 2, False],
          [[i for i in range(90)], 8, True , 12]
         ]



def test_trouve () :
  print('Test trouve:')
  score = 0
  data = test_trouveData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = trouve(T,x)
    if res == ref :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    compte  : %d' % res)
      print('    attendu : %d' % ref)
  print('* Score : %d/%d\n' % (score, ldata))


############################################################
#
# Tests : trouveOps
#


def test_trouveOpsData():  
  return [[[1,2,3,4,5], 2, True, 3],
          [[1,2,2,4,5,7,10,11,11,12,14,14,15,15,20], 6, False, 8],
          [[1,3,5,7,9], 5, True, 2],
          [[1,3,5,7,9], 2, False, 10],
          [[i for i in range(0 ,90 , 3)], 8, False, 16], 
          [[i for i in range(0 ,90 , 3)], 3, True, 11],
          [[1]+[2]*100000,1,True, 50],
          [[1]+[2]*100000,2,True, 2]
         
         ]




def test_trouveOps () :
  print('Test trouveOps:')
  score = 0
  data = test_trouveOpsData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    refOps = dt[3]
    res,ops = trouveOps(T,x)
    if res == ref  and refOps <= ops:
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    trouve  : %s (en %d ops)' % (str(res),ops))
      print('    attendu : %s (en au moins %d ops)' % (str(ref),refOps))
  print('* Score : %d/%d\n' % (score, ldata))


    
############################################################
#
# Tests : trouvePremier
#

def test_trouvePremierData():
  return [[[1],1,0],
          [[1]+[2]*100000,1,0],
          [[1]+[2]*100000,2,1],
          [[i for i in range(0 ,90 , 3)], 2, False],
          [[i for i in range(0 ,90 , 3)], 90, False],
          [[i for i in range(0 ,90 , 3)], 84, 28],
          [[i for i in range(0 ,90 , 3)], 15, 5],
          [[i for i in range(0 ,90 , 3)], 80, False], 
          [[i for i in range(0 ,90 , 3)], 3, 1 ],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,4,5,6,7,7],2,23] 
         ]
    

def test_trouvePremier () :
  print('Test trouvePremier:')
  score = 0
  data = test_trouvePremierData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = trouvePremier(T,x)
    if res == ref :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    trouve  : %s' % str(res))
      print('    attendu : %s' % str(ref))
  print('* Score : %d/%d\n' % (score, ldata))


from math import log,floor

def test_trouvePremierOps () :
  print('Test trouvePremierOps:')
  score = 0
  data = test_trouvePremierData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res,ops = trouvePremierOps(T,x)
    logLen = floor(log(max(len(T),2),2))
    if res == ref and (len(T)<2 or logLen<=ops<=6*(logLen+1)):
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    trouve  : %s (en %d ops)' % (str(ref),ops))
      if ops<logLen:
        print('    attendu : %s (en au moins %d ops)' % (str(ref),logLen))
      else :
        print('    attendu : %s (moins de %d ops)' % (str(ref),5*logLen))
  print('* Score : %d/%d\n' % (score, ldata))

def test_occurrenceDichotomieData():
  return [[[1],1,1],
          [[1,2,2,3,3,4,4,4,5],3,2],
          [[1,2,2,3,3,4,4,4,5],1,1],
          [[1,2,2,3,3,4,4,4,5],0,0],
          [[],12,0],
          [[1]*1000+[2],1,1000],
          [[1]+[2]*100000,2,100000],
          [[1]+[2]*100000,1,1],
          [[i for i in range(10)],4,1]]
#          [[i for i in range(1,10**5,2)],42*42,False]]
    

def test_occurrenceDichotomie () :
  print('Test occurrenceDichotomie:')
  score = 0
  data = test_occurrenceDichotomieData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = occurrenceDichotomie(T,x)
    if type(res)==type(ref) and res == ref :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    trouve  : %s' % str(res))
      print('    attendu : %s' % str(ref))
  print('* Score : %d/%d\n' % (score, ldata))
  


def occurrenceDichotomieOpsData():
    return [[[1],1,5],
          [[1,2,2,3,3,4,4,4,5],3,15],
          [[1,2,2,3,3,4,4,4,5],1,17],
          [[1,2,2,3,3,4,4,4,5],0,17],
          [[],12,1],
          [[1]*1000+[2],1,41],
          [[1]+[2]*100000,2,67],
          [[1]+[2]*100000,1,69],
          [[i for i in range(10)],4,14]]
    

def test_occurrenceDichotomieOps() :
  print('Test occurrenceDichotomieOps:')
  score = 0
  data = occurrenceDichotomieOpsData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    T = dt[0]
    x = dt[1]
    opsdata = dt[2]
    res,ops = occurrenceDichotomieOps(T,x)
    if type(ops)==type(opsdata) and ops == opsdata :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    trouve  : %s' % str(ops))
      print('    attendu : %s' % str(opsdata))
  print('* Score : %d/%d\n' % (score, ldata))  

if __name__ == '__main__':
  test_trouve()
  test_trouveOps()
  test_trouvePremier()
  test_trouvePremierOps()
  test_occurrenceDichotomie()
  test_occurrenceDichotomieOps()
  test_comparOccurrenceOps()
