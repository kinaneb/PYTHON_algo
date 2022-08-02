#!/usr/bin/env python3

import random
from time import clock
import matplotlib.pyplot as plt

# Exercice 1

def triSelection(T):
    # A COMPLETER
    for i in range(len(T)):
      min = i
      for j in range(i,len(T)):
        if T[j] < T[min]:
          min = j
      T[i], T[min] = T[min], T[i]
    return T

def randomPerm(n):
    # A COMPLETER
    res = list(range(1,n+1))
    for i in range(n-1):
      p = random.randint(i,n-1)
      if(p != i): res[i], res[p] = res[p], res[i]
    '''
    for j in range(len(temp)):
      p = random.randrange(len(temp))
      res.append(temp[p])
      temp = temp[:-1]
    '''
    return res

def testeQueLaFonctionTrie(f):
    # A COMPLETER
    n = random.randint(2,100)
    T = randomPerm(n)
    temp = T
    T_trie = triSelection(T)
    for (i,elt) in enumerate(T_trie):
      if (elt != i+1):
        print("tableau avan trié ",temp)
        print("tableau aprés trié",T_trie)
        print("tableau attendu ", list(range(1,n+1)))
        return False
    return True

def randomTab(n,a,b):
    # A COMPLETER
    res = []
    for i in range (n):
      res.append(random.randint(a,b))
    return res

def derangeUnPeu(n,k,rev = True):
    # A COMPLETER
    res = list(range(1,n+1))
    if rev: res = res[::-1]
    for i in range(k):
      p1, p2 = random.randrange(n), random.randrange(n)
      if(p1 != p2 ): res[p1], res[p2] = res[p2], res[p1]
    return res

# Exercice 2

def triInsertionEchange(T):
    # A COMPLETER
    if (len(T) < 2): return T
    for i in range (1,len(T)):
        v = T[i]
        j = i-1
        while T[j] > v and j >=0 :
            T[j+1] = T[j]
            j -= 1
        T[j+1] = v
    return T

def triInsertionRotation(T):
    # A COMPLETER
    for i in range(len(T)):
        for j in range (i, -1, -1):
            if (T[i] > T[j]):
                T = T[:j+1] + [T[i]] + T[j+1:i] + T[i+1:]
                i -= 1
                break
            if (T[i] <= T[0]):
                T = [T[i]] + T[:i] + T[i+1:]
                i -= 1
                break
    return T
########################################
#
# fonction aux
########################################
def trouvePlusPetit(T,x):
    if (len(T) == 0): return False
    m = len(T)//2
    if (x <= T[m]) : return True
    trouvePlusPetit(T[m+1:],x)

def trouvePosition(T,x, debut=0):
    if (len(T) == 0): return False
    m = len(T)//2
    debut += m
    if (x <= T[m]):
        if not trouvePlusPetit(T[:m],x): return debut
        else: return trouvePosition(T[:m], x, debut - m)
    else:
        if not trouvePlusPetit(T[m:], x): return len(T)
        else: return trouvePosition(T[m:], x, debut)

def triInsertionRapide(T):
    # A COMPLETER
    for i in range(1,len(T)):
        p = trouvePosition(T[:i], T[i])
        if not (p == len(T[:i])):
            T = T[:p] + [T[i]] + T[p:i] + T[i+1:]
    return T

def fusion(T1,T2):
    i, j = 0, 0
    res = []
    while (i < len(T1) and j < len(T2) ):
        if (T1[i] <= T2[j]):
            res += [T1[i]]
            i += 1
        else:
            res += [T2[j]]
            j += 1
    if (i < len(T1)): res += T1[i:]
    elif ( j < len(T2)): res += T2[j:]
    return res

def triFusion(T) :
    # A COMPLETER
    if (len(T)==1):return T
    m = len(T)//2
    return fusion(triFusion(T[:m]),triFusion(T[m:]))

def triBulles(T) :
    # A COMPLETER
    for i in range(len(T)):
        for j in range(0,i):
            if (T[i] < T[j]):
                T[i], T[j] = T[j], T[i]
    return T

#######################################################################
#######################################################################
#
#  tp 6
#######################################################################
#######################################################################

#######################################################################
#
# tp 6 ex 1

#################################################################
#
# tri rapide avec mémoire auxiliaire pivot [0]
#################################################################
def partion(T) :
    pivot = T[0]
    gouche = [e for e in T if e < pivot]
    droite = [e for e in T if e > pivot]
    return pivot , gouche, droite

def triRapide_Aux(T) :
    if (len(T) < 2) : return T
    pivot, gouche, droite = partion(T)
    return gouche + [pivot] + droite

#################################################################
# 
# tri rapide en place pivot [0]
#################################################################
def partion_EnP(T, debut, fin) :
    if (fin - debut == 2) and (T[debut] < T[debut + 1]): return debut + 1
    pivot, gouche, droite = T[debut], debut + 1, fin
    while (gouche <= droite) : 
        if (T[gouche] < pivot) : gouche += 1
        elif (T[droite] >= pivot) : droite -= 1
        else : T[gouche], T[droite] = T[droite], T[gouche]
    T[debut], T[droite] = T[droite], pivot
    return droite


def triRapide_EnP_Aux(T, debut, fin) :
    if (fin- debut < 2): return T
    indice_Pivot = partion_EnP(T, debut, fin)
    triRapide_EnP_Aux(T, debut, indice_Pivot)
    triRapide_EnP_Aux(T, indice_Pivot + 1, fin)
    return T 

def triRapide_EnP(T) : 
    if (len(T) < 2) : return T
    return triRapide_EnP_Aux(T, 0, len(T)-1)


#################################################################
#
# tri rapide avec mémoire auxiliaire pivot [aléatoire]
#################################################################
def partion_a(T) :
    r = random.randint(0,len(T)-1)
    pivot = T[r]
    gouche = [e for e in T if e < pivot]
    droite = [e for e in T if e > pivot]
    return pivot , gouche, droite

def triRapide_Aux_a(T) :
    if (len(T) < 2) : return T
    pivot, gouche, droite = partion_a(T)
    return gouche + [pivot] + droite

#################################################################
# 
# tri rapide en place pivot [aléatoire]
#################################################################
def partion_EnP_a(T, debut, fin) :
    if (fin - debut == 2) and (T[debut] < T[debut + 1]): return debut + 1 
    r = random.randint(debut,len(T)-1)
    T[r], T[debut] = T[debut], T[r]
    pivot, gouche, droite = T[debut], debut + 1, fin
    while (gouche <= droite) : 
        if (T[gouche] < pivot) : gouche += 1
        elif (T[droite] >= pivot) : droite -= 1
        else : T[gouche], T[droite] = T[droite], T[gouche]
    T[debut], T[droite] = T[droite], pivot
    return droite


def triRapide_EnP_Aux_a(T, debut, fin) :
    if (fin - debut < 2): return T
    indice_Pivot = partion_EnP(T, debut, fin)
    triRapide_EnP_Aux_a(T, debut, indice_Pivot)
    triRapide_EnP_Aux_a(T, indice_Pivot + 1, fin)
    return T 

def triRapide_EnP_a(T) : 
    if (len(T) < 2) : return T
    return triRapide_EnP_Aux_a(T, 0, len(T)-1)


#######################################################################
#
# tp 6 ex 2

#################################################################
# 
# tri rapide en place pivot [aléatoire] Ameliore
#################################################################
def triRapideAmeliore(T):
    if (len(T) < 15): return triInsertionEchange(T)
    else: return triRapide_EnP_Aux_a(T, 0, len(T)-1)

#################################################################
# 
# tri rapide Incomplet en place pivot [aléatoire] Ameliore 
# si len(T) => 15 else rien
#################################################################
def triRapideIncomplet(T):
    if (len(T) < 15) : 
        return T
    else : return triRapide_EnP_Aux(T, 0, len(T)-1)

#################################################################
# 
# tri insertion pour le résulta de triRapideIncomplet
#################################################################
def triSedgewick(T):
    T = triRapideIncomplet(T)
    return triInsertionEchange(T)


#######################################################################
#
# tp 6 ex 3

################################################################
#
# gap = ..,  [..., debut,..elt,..elt,..elt,..elt,]
################################################################
def triInsertionPartiel(T, gap, debut):
    if (len(T) < debut+gap): return T
    for i in range (debut,len(T),gap):
        v = T[i]
        j = i-gap
        while T[j] > v and j >= debut :
            T[j+gap] = T[j]
            j -= gap
        T[j+gap] = v
    return T

################################################################
#
# triShell
################################################################
def triShell(T):
    H =[57,23,10,4,1]
    for i in H:
        T = triInsertionPartiel(T,i,0)
    return T

##############################################################################
#
# Mesure du temps
#

def mesure(algo, T) :
    debut = clock()
    algo(T)
    return clock() - debut

def mesureMoyenne(algo, tableaux) :
  return sum([ mesure(algo, t[:]) for t in tableaux ]) / len(tableaux)

couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y', '#ff7f00', '.5', '#00ff7f', '#7f00ff', '#ff007f', '#7fff00', '#007fff' ]
marqueurs = ['o', '^', 's', '*', '+', 'd', 'x', '<', 'h', '>', '1', 'p', '2', 'H', '3', 'D', '4', 'v' ]

def courbes(algos, tableaux, styleLigne='-') :
  x = [ t[0] for t in tableaux ]
  for i, algo in enumerate(algos) :
    print('Mesures en cours pour %s...' % algo.__name__)
    y = [ mesureMoyenne(algo, t[1]) for t in tableaux ]
    plt.plot(x, y, color=couleurs[i%len(couleurs)], marker=marqueurs[i%len(marqueurs)], linestyle=styleLigne, label=algo.__name__)

def affiche() :
  plt.xlabel('taille du tableau')
  plt.ylabel('temps d\'execution')
  plt.legend(loc='upper left')

  if (algos != algos_rapid and algos != algos_rapid_a and algos != algos_shell):
    plt.title('>>>Pour Effectuer Le Test De tp6 Ex1\nEffacez Le # Dans Le Ligne: 362 SVP', fontweight='bold', loc='left')
  elif (algos == algos_rapid):
    plt.title('>>>Pour Effectuer Le Test De tp6 Ex2\nEffacez Le # Dans Le Ligne: 367 SVP', fontweight='bold', loc='left')
  elif (algos == algos_rapid_a):
    plt.title('>>>Pour Effectuer Le Test De tp6 Ex3\nEffacez Le # Dans Le Ligne: 372 SVP', fontweight='bold', loc='left')
 
  plt.show()
  
##############################################################################
#
# Main
#

if __name__ == '__main__':
  # LIGNE A COMPLETER
  algos = [triSelection, triInsertionEchange, triInsertionRotation, triInsertionRapide, triFusion, triBulles] # chaque case contient un algorithme de tri différent

#########################################
#
# test tp 6
####################################### 
  algos_rapid = [triRapide_Aux, triRapide_EnP, triRapide_Aux_a, triRapide_EnP_a]
  algos_rapid_a = [triRapideAmeliore, triSedgewick]
  algos_shell =  [triSelection, triInsertionEchange, triInsertionRotation, triInsertionRapide, triFusion, triShell]

  #######################################################
  #  "pour effectuer le test de tp6 ex 1, 
  #   effacez le # dans le ligne: 356 SVP"
  #algos = algos_rapid

  #######################################################
  #  "pour effectuer le test de tp6 ex 2, 
  #   effacez le # dans le ligne: 361 SVP"
  #algos = algos_rapid_a

  #######################################################  
  #  pour effectuer le test de tp6 ex 3, 
  #  effacez le # dans le ligne: 366 SVP"
  #algos = algos_shell


  for tri in algos :
      if testeQueLaFonctionTrie(tri):
          print(tri.__name__ + ": OK")
      else:
          print(tri.__name__ + ": échoue")
  taille = 1000 # taille maximale des tableaux à trier
  pas = 100 # pas entre les tailles des tableaux à trier
  ech = 5 # taille de l'échantillon pris pour faire la moyenne
  print()
  print("Comparaison à l'aide de randomPerm")
  tableaux = [[i, [randomPerm(i) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche()
  print()
  print("Comparaison à l'aide de randomTab")
  # A COMPLETER
  tableaux2 = [[i, [randomTab(i, 1, taille) for j in range(ech)]] for i in range(2, taille, pas)    ]
  courbes(algos, tableaux2, styleLigne=':')
  affiche()
  print("Comparaison à l'aide de derangeUnPeu (rev = False)")
  # A COMPLETER
  tableaux3 = [[i, [derangeUnPeu(100, i, False) for j in range(ech)]] for i in range(2, 100, 10)    ]
  courbes(algos, tableaux3, styleLigne='-.')
  affiche()
  print("Comparaison à l'aide de derangeUnPeu (rev = True)")
  # A COMPLETER
  tableaux3 = [[i, [derangeUnPeu(100, i) for j in range(ech)]] for i in range(    2, 100, 10)    ]
  courbes(algos, tableaux3, styleLigne='-.')
  affiche()
