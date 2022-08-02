#!/usr/local/bin/python3

from os import system

# *******************************
# ** Quelques fonctions utiles **
# *******************************

def nouvelABRVide() :
  return [[None,None,None,None]]

def estVide(arbre) :
  if arbre == [] or arbre == [[None,None,None,0]] or arbre == [[None,None,None,None]]: return True
  return False

def pere(arbre, i) :
  ''' retourne l'indice du pere (ou None) '''
  return arbre[i][3]

def estRacine(arbre,i):
  ''' retourne True si le noeud d'indice i est la racine de l'arbre '''
  return arbre[i][3] == None

def estFilsGauche(arbre,i):
  # retourne True si le noeud d'indice i est fils gauche de son pere
  return arbre[arbre[i][3]][1] == i

def estFilsDroit(arbre,i):
  # retourne True si le noeud d'indice i est fils droit de son pere
  return arbre[arbre[i][3]][2] == i

def estFeuille(arbre,i):
  # retourne True si le noeud d'indice i est une feuilles vide [None,None,None,_]
  if arbre[i][0] == arbre[i][1] and arbre[i][1] == arbre[i][2] and arbre[i][2] == None: return True
  return False

# retourne l'indice de la racine si elle existe
def racine(arbre) :
  for i in range(len(arbre)):
    if estRacine(arbre,i) : return i
  return None

# retourne une copie de l'arbre
def copier(arbre):
  copie = []
  for noeud in arbre : copie.append(noeud[:])
  return copie

#echange les noeuds stockés en i et j en maintenant tous les liens
def swap(arbre,i,j):
  if i==j : return

  aChanger = [i,j]
  for x in i,j :
    for y in 1,2,3 :
      if arbre[x][y] != None and arbre[x][y] not in aChanger :
        aChanger.append(arbre[x][y])
        
  arbre[i],arbre[j] = arbre[j],arbre[i] #echange tout, étiquettes, etc

  for x in aChanger :
    for y in 1,2,3 :
      if arbre[x][y] == i :
        arbre[x][y] = j
      elif arbre[x][y] == j :
        arbre[x][y] = i

#supprime les noeuds stockés dans le tableau idx (sans perturber les liens des autres noeuds)
def suppr(arbre, idx):
  toDel = len(idx)
  toMove = []
  lasts = [False]*toDel
  n = len(arbre)
  for i in idx :
    if i >= n - toDel :
      lasts[n - 1 - i] = True
    else :
      toMove.append(i)

  for k in range(toDel) :
    if not lasts[k] :
      swap(arbre,toMove.pop(),n-1-k)
      
  for i in range(toDel) :
    arbre.pop()

##########################################################################
# Tester si deux arbres sont identiques (à encodage près)

def egalite_aux(a1,i1,a2,i2):
  #Cas de 2 feuilles sans étiquettes
  if a1[i1][0] == None and a2[i2][0] == None: return True
  #Cas d'une feuille sans étiquette et d'un vrai noeuf
  if a1[i1][0] != None and a2[i2][0] == None: return False
  if a1[i1][0] == None and a2[i2][0] != None: return False
  
  if estFeuille(a1,i1):
    if estFeuille(a2,i2):
      return a1[i1][0] == a2[i2][0]
    else:
      return False
  if estFeuille(a2,i2):
    if estFeuille(a1,i1):
      return a1[i1][0] == a2[i2][0]
    else:
      return False
  else:
    if a1[i1][0] != a2[i2][0] : return False
    else:
      return egalite_aux(a1,a1[i1][1],a2,a2[i2][1]) and egalite_aux(a1,a1[i1][2],a2,a2[i2][2])

def egalite(a1,a2):
  if estVide(a1):
    return estVide(a2)
  if estVide(a2):
    return estVide(a1)
  r1 = racine(a1)
  r2 = racine(a2)
  return egalite_aux(a1,r1,a2,r2)

##########################################################################

##########################################################################
def arbreBinaireDeFichier(fichier) :
  ''' lit un fichier contenant la description d'un arbre avec une ligne
  par noeud, au format : num,etiquette,fg,fd
  et construit un tableau contenant en case d'indice num la liste
  [etiquette, fg, fd, pere] ''' 
  try:
    res = []
    with open(fichier) as f:
      for ligne in f :
        noeud = [None, None, None, None]
        num, etiquette, fg, fd = ligne.strip().split(',')
        noeud[0] = None if etiquette == '' else etiquette 
        if fg : noeud[1] = int(fg)
        if fd : noeud[2] = int(fd)
        res.append(noeud)
  except IOError:
    print("Erreur d'ouverture du fichier <%s>" % nom_fich)
    return
  # ajout des pères
  for i, noeud in enumerate(res) :
    etiquette, fg, fd, pere = noeud
    for fils in (fg, fd) : 
      if fils != None : res[fils][-1] = i
  # la racine est son propre père
  # for i, noeud in enumerate(res) :
  #   if noeud[-1] == None : 
  #     noeud[-1] = i
  #     break
  return res
##########################################################################
  
##########################################################################
def arbreBinaireVersFichier(arbre, fichier) :
  ''' réciproque de la précédente '''
  try :
    with open(fichier, 'w') as f:
      for i, noeud in enumerate(arbre) :
        etiquette, fg, fd, pere = noeud
        f.write(str(i) + ',')
        if etiquette != None : f.write(str(etiquette))
        f.write(',')
        if fg != None : f.write(str(fg))
        f.write(',')
        if fd != None : f.write(str(fd))
        f.write('\n')
  except IOError:
    print("Erreur d'ouverture du fichier <%s>" % fichier)
##########################################################################
  

##########################################################################
def etiquetteStr2Int(arbre) :
  ''' transforme les étiquettes de type str (représentant des entiers) en
  étiquettes de type int '''
  for i, noeud in enumerate(arbre) :
    if noeud != None and noeud[0] != None :
      arbre[i][0] = int(noeud[0])	# pas de vérification d'erreur... tant pis 
  return arbre
##########################################################################
  

##########################################################################
def completeArbreBinaire(arbre) :
  ''' ajoute des feuilles vides tout autour de l'arbre binaire ''' 
  taille = len(arbre)
  if taille == 0 :
    arbre.append([None, None, None, None])
    return arbre
  for i in range(taille) : 
    for j in (1, 2) :
      if arbre[i][j] == None : 
        arbre[i][j] = len(arbre)
        arbre.append([None, None, None, i])
  return arbre
##########################################################################


##########################################################################
def arbreBinaireEntierCompletDeFichier(fichier) :
  return completeArbreBinaire(etiquetteStr2Int(arbreBinaireDeFichier(fichier)))
##########################################################################

##########################################################################
def dessineArbreBinaire(arbre,fname = '/tmp/arbre') :
  ''' crée un fichier fname.dot et un fichier fname.pdf
  représentant l'arbre ''' 
  racine = None
  for i, noeud in enumerate(arbre) : 
    if noeud[-1] == None : racine = i
  if racine == None : 
    print("Erreur, il manque une racine")
    return

  # creation du fichier .dot
  etiquette, fg, fd, pere = arbre[racine]
  if etiquette :
    fic = open(fname+".dot", 'w')
    fic.write("graph arbre {\n")
    fic.write("\t" + str(racine) + "[label=" + str(etiquette) + "];\n")
    todo = [fg, fd]
  else : 
    return
  while todo != [] :
    i = todo.pop(0)
    # cas non complete
    if i == None : continue
    # cas general
    etiquette, fg, fd, pere = arbre[i]
    if etiquette :
      todo += [fg, fd]
      fic.write("\t" + str(i) +"[label=" + str(etiquette) + "];\n")
    else :
      fic.write("\t" + str(i) + '[shape="plaintext", label=""];\n')
    fic.write("\t" + str(pere) + " -- " + str(i) + ";\n")
  fic.write("}\n")
  fic.close()

  # transformation en .pdf
  system("dot -Tpdf -o " + fname + ".pdf " + fname + ".dot")
##########################################################################
  
##########################################################################
arbreVide = completeArbreBinaire([])

arbre3ABR1 = completeArbreBinaire([[2, 1, 2, None], [1, None, None, 0], [3, None, None, 0]])
arbre3ABR2 = completeArbreBinaire([[1, None, 1, None], [2, None, 2, 0], [3, None, None, 1]])
arbre3ABR3 = completeArbreBinaire([[3, 1, None, None], [2, 2, None , 0], [1, None, None, 1]])

arbre10ABR1 = arbreBinaireEntierCompletDeFichier("abr10_1.txt")
arbre10ABR2 = arbreBinaireEntierCompletDeFichier("abr10_2.txt")

arbre100ABR1 = etiquetteStr2Int(arbreBinaireDeFichier("abr100_1.txt"))
arbre100ABR2 = etiquetteStr2Int(arbreBinaireDeFichier("abr100_2.txt"))

##########################################################################
  
##########################################################################
if __name__ == '__main__':
  pass
