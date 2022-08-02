#!/usr/local/bin/python3

from os import system

          (arbrePlanetesComplet, ['Saturne', 'Mars', 'Jupiter', 'Neptune', 'Mercure', 'Pluton', 'Terre', 'Uranus', 'Vénus']),


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
        noeud[0] = etiquette
        if fg : noeud[1] = int(fg)
        if fd : noeud[2] = int(fd)
        res.append(noeud)
  except IOError:
    print("Erreur d'ouverture du fichier <%s>" % nom_fich)
    return
  # ajout des peres  
  for i, noeud in enumerate(res) :
    etiquette, fg, fd, pere = noeud
    for fils in (fg, fd) : 
      if fils != None : res[fils][-1] = i
  return res
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
def dessineArbreBinaire(arbre,fname = '/tmp/arbre') :
  ''' cree un fichier fname.dot et un fichier fname.pdf
  representant l'arbre ''' 
  racine = None
  for i, noeud in enumerate(arbre) : 
    if noeud[-1] == None : racine = i
  if racine == None : 
    print("Erreur, il manque une racine")
    return

  # creation du fichier .dot
  etiquette, fg, fd, pere = arbre[racine]
  if etiquette != None :
    fic = open(fname+".dot", 'w')
    fic.write("graph arbre {\n")
    fic.write("\t" + str(racine) + "[label=" + etiquette + "];\n")
    todo = [fg, fd]
  else : 
    return
  while todo != [] :
    i = todo.pop(0)
    # cas non complete
    if i == None : continue
    # cas general
    etiquette, fg, fd, pere = arbre[i]
    if etiquette != None :
      todo += [fg, fd]
      fic.write("\t" + str(i) +"[label=" + etiquette + "];\n")
    else :
      fic.write("\t" + str(i) + '[shape="plaintext", label=""];\n')
    fic.write("\t" + str(pere) + " -- " + str(i) + ";\n")
  fic.write("}\n")
  fic.close()

  # transformation en .pdf
  system("dot -Tpdf -o " + fname + ".pdf " + fname + ".dot")
##########################################################################
  
##########################################################################
arbreVide = []
arbreVideComplet = [[None, None, None, None]]

arbreFeuille = [['a', None, None, None]]
arbreFeuilleComplet = [['a', 1, 2, None], [None, None, None, 0], [None,
  None, None, 0]]

arbreFilGauche = [['a', 1, None, None], ['b', 2, None, 0], ['c', None, None, 1]]
arbreFilDroit = [['a', None, 1, None], ['b', None, 2, 0], ['c', None, None, 1]]

arbreParfait = [['a', 1, 2, None], ['b', None, None, 0], ['c', None, None, 0]]

arbrePlanetes = arbreBinaireDeFichier('planetes.txt')
#[['Saturne', 1, 6, None], ['Mars', 2, 3, 0], ['Jupiter', None, None, 1], ['Neptune', 4, 5, 1], ['Mercure', None, None, 3], ['Pluton', None, None, 3], ['Terre', None, 7, 0], ['Uranus', None, 8, 6], ['Vénus', None, None, 7]]
arbrePlanetesComplet = completeArbreBinaire(arbreBinaireDeFichier('planetes.txt'))
#[['Saturne', 1, 6, None], ['Mars', 2, 3, 0], ['Jupiter', 9, 10, 1], ['Neptune', 4, 5, 1], ['Mercure', 11, 12, 3], ['Pluton', 13, 14, 3], ['Terre', 15, 7, 0], ['Uranus', 16, 8, 6], ['Vénus', 17, 18, 7], [None, None, None, 2], [None, None, None, 2], [None, None, None, 4], [None, None, None, 4], [None, None, None, 5], [None, None, None, 5], [None, None, None, 6], [None, None, None, 7], [None, None, None, 8], [None, None, None, 8]]

arbreFilsGaucheComplet = [['8', 1, 2, None], ['5', 3, 4, 0], [None, None, None, 0], [None, None, None, 1], [None, None, None, 1]]

arbreABR = [['1', 6, 7, 3], ['6', 8, 9, 3], ['9', 10, 11, 4], ['5', 0, 1, 5], ['10', 2, 12, 5], ['8', 3, 4, None], [None, None, None, 0], [None, None, None, 0], [None, None, None, 1], [None, None, None, 1], [None, None, None, 2], [None, None, None, 2], [None, None, None, 4]]
arbreNABR = [['1', 6, 7, 3], ['6', 8, 9, 3], ['8', 10, 11, 4], ['5', 0, 1, 5], ['10', 2, 12, 5], ['8', 3, 4, None], [None, None, None, 0], [None, None, None, 0], [None, None, None, 1], [None, None, None, 1], [None, None, None, 2], [None, None, None, 2], [None, None, None, 4]]

##########################################################################
  
##########################################################################
if __name__ == '__main__':
  #print('arbre lu dans le fichier :')
  #print(arbrePlanetes)
  #print('arbre apres completion :')
  print(arbreNABR)
  #dessineArbreBinaire(arbrePlanetesComplet)
  dessineArbreBinaire(arbreNABR)
  print('ouvrir le fichier /tmp/arbre.pdf pour une representation graphique')
