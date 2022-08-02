#!/usr/bin/env python3

from os import system
from random import shuffle
from copy import deepcopy
from random import randint
import numpy as np
import matplotlib.pyplot as plt
 
class Bnoeud :

    # constructeur : le premier paramètre est l'objet à construire;
    # il s'appelle self par convention
    def __init__(self, cles=[], fils=None, pere=None, p=1) :
        ''' ce constructeur ne fait pas de vérification de cohérence
        (entre p et les nbs de clés et de fils) '''
        self.nbCles = len(cles)
        self.nbFils = 0 if fils == None else len(fils)
        # normalement, nbFils = nbCles+1 (sauf pour les feuilles), mais
        # cela peut momentanément ne pas être le cas au cours d'une opération
        self.cles = cles + [None] * (2*p-self.nbCles)
        self.fils = None if fils == None else fils + [None] * (2*p+1-self.nbFils)
        self.attache_les_fils()
        self.pere = pere
    
    # les feuilles n'ont pas de fils
    # comme pour le constructeur, les méthodes ont l'objet concerné comme
    # premier paramètre
    def estFeuille(self) :
        return (self.fils == None)

    def attache_les_fils(self) :
        ''' met à jour le champ pere de tous les fils '''
        if self.fils != None :
          for f in self.fils[:self.nbFils] : 
            f.pere = self
    
    def supprime_cle(self, i) :
        ''' supprime la clé d'indice i et met à jour le nombre de clés '''
        if i<0 or i>=self.nbCles : return None
        res = self.cles[i]
        self.cles[i:self.nbCles] = self.cles[i+1:self.nbCles] + [None]
        self.nbCles -= 1
        return res

    def supprime_fils(self, i) :
        ''' supprime le fils d'indice i et met à jour le nombre de fils '''
        if i<0 or i>=self.nbFils : return None
        res = self.fils[i]
        self.fils[i:self.nbFils] = self.fils[i+1:self.nbFils] + [None]
        self.nbFils -= 1
        return res

    def insere_cle(self, i, x) :
        ''' insère la clé x en position i et met à jour le nombre de clés 
        (vérifie que le nombre de clés permet l'insertion, 
        mais pas que la position i est adaptée) '''
        if self.nbCles >= len(self.cles): return None
        if i<0 or i>self.nbCles : return None
        self.cles[i:self.nbCles+1] = [x] + self.cles[i:self.nbCles]
        self.nbCles += 1
        return x

    def insere_fils(self, i, noeud) :
        ''' insère un noeud comme fils en position i et met à jour le
        nombre de fils
        (vérifie que le nombre de fils permet l'insertion, 
        mais pas que la position i est adaptée) '''

        # if self.nbFils >= len(self.fils): return None 

        if self.nbFils > len(self.cles): return None
        if i<0 or i>self.nbFils : return None
        self.fils[i:self.nbFils+1] = [noeud] + self.fils[i:self.nbFils]
        self.nbFils += 1
        noeud.pere = self
        return noeud

    ###fonction Aux ************************** 

    def vide_cles(self) :
        self.cles = [None] * (self.nbCles)
        self.nbCles = 0

    def vide_fils(self) :
        self.fils = []
        self.nbFils = 0


    def contient(self, x) :
        ''' teste si le noeud contient la clé x
        retourne (True, i) si cles[i]==x et (False, i) si cles[i-1] < x < cles[i]
        '''
        #
        # À COMPLÉTER
        #
        if self.cles[0] == None:
            return False, 0
        if (self.cles[0] != None and x < self.cles[0]):
            return False, 0
        if (self.cles[-1] != None and x > self.cles[-1]):
            return False, len(self.cles)
        for i, e in enumerate(self.cles):
            if x == e:
                return True, i 
            if (self.cles[i + 1] == None or x < self.cles[i + 1]):
                return False, (i + 1)
        return False, -1

    def cherche(self, x) : 
        ''' cherche x dans le sous-arbre de racine self '''
        #
        # À COMPLÉTER
        #
        contient, i = self.contient(x)
        if contient: return contient, self, i
        elif (self.nbFils > i):
            return self.fils[i].cherche(x)
        else: return contient, self, i   


class Barbre :

    def __init__(self, bnoeud=None, p=1) :
        self.racine = bnoeud if bnoeud != None else Bnoeud(p=p)
        self.ordre = p


    def dessine(self, fname = '/tmp/arbre') :
        ''' crée un fichier fname.dot et un fichier fname.pdf représentant l'arbre ''' 
        
        # creation du fichier .dot
        fic = open(fname+".dot", 'w')
        fic.write("graph arbre {\n")
        
        cpt = 0
        todo = [(cpt, self.racine)]
        aretes = []
        
        while todo != [] :
            numero, tmp = todo.pop(0)
            fic.write("\t" + str(numero) +'[label="'+ str(tmp.cles[0]))
            for k in tmp.cles[1:tmp.nbCles] : fic.write(', ' + str(k))
            fic.write('"];\n')
            if tmp.fils != None :
                for f in tmp.fils[:tmp.nbFils] :
                    cpt += 1
                    aretes.append((numero, cpt))
                    todo.append((cpt, f))
                        
        for i,j in aretes :
            fic.write("\t" + str(i) + " -- " + str(j) + ";\n")
           
        fic.write("}\n")
        fic.close()
       
        # transformation en .pdf
        system("dot -Tpdf -o " + fname + ".pdf " + fname + ".dot")
  

    def cherche(self, x) :
        ''' retourne (True, noeud, i) si x == noeud.cles[i]
        et (False, feuille, i) si x n'est pas dans l'arbre mais devrait
        être inséré en feuille.cles[i] '''
        return self.racine.cherche(x)



    def Bnoeud_scinde(self, x, g, d, f, iFils) :
        p=self.ordre
        if f.pere != None :
            pere = f.pere
            f.supprime_fils(iFils)
            tmpCles = deepcopy(f.cles)
            tmpFils = deepcopy(f.fils)
            iFils1 = pere.fils.index(f)
            tmpFils.insert(iFils,d)
            tmpFils.insert(iFils,g)
            tmpCles.append(x)
            tmpCles.sort()
            g1 = Bnoeud(cles=tmpCles[0:p], fils=tmpFils[0:p+1], pere=f.pere, p=p)
            d1 = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=tmpFils[p+1:2*p+2], pere=f.pere, p=p)
            if pere.nbFils < 2*p+1 :
                pere.supprime_fils(iFils1)
                pere.insere_fils(iFils1, g1)
                pere.insere_fils(iFils1+1, d1)
                pere.insere_cle(iFils1, tmpCles[p])
            else:
                self.Bnoeud_scinde(tmpCles[p], g1, d1, pere, iFils1)
        else:
            f.supprime_fils(iFils)
            tmpCles = deepcopy(f.cles)
            tmpFils = deepcopy(f.fils)
            tmpFils.insert(iFils,d)
            tmpFils.insert(iFils,g)
            f.vide_cles()
            f.vide_fils()
            tmpCles.append(x)
            tmpCles.sort()
            g1 = Bnoeud(cles=tmpCles[0:p], fils=tmpFils[0:p+1], pere=f, p=p)
            d1 = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=tmpFils[p+1:2*p+2], pere=f, p=p)
            f.insere_cle(0,tmpCles[p])
            f.insere_fils(0,g1)
            f.insere_fils(1,d1)

    def feuille_scinde(self,x,f):
        p=self.ordre
        if f.pere != None :
            pere = f.pere 
            tmpCles = deepcopy(f.cles)
            tmpFils = deepcopy(f.fils)
            iFils = pere.fils.index(f)
            tmpCles.append(x)
            tmpCles.sort()
            g = Bnoeud(cles=tmpCles[0:p], fils=None, pere=pere, p=p)
            d = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=None, pere=pere, p=p)
            if pere.nbFils < 2*p+1 :
                pere.supprime_fils(iFils)
                pere.insere_fils(iFils, d)
                pere.insere_fils(iFils, g)
                pere.insere_cle(iFils, tmpCles[p])
            else :
                self.Bnoeud_scinde(tmpCles[p], g, d, pere, iFils)
        else :
            tmpCles = deepcopy(f.cles)
            tmpFils = deepcopy(f.fils)
            f.vide_cles()
            f.vide_fils()
            tmpCles.append(x)
            tmpCles.sort()
            g = Bnoeud(cles= tmpCles[0:p], fils=None, pere=f, p=p)
            d = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=None, pere=f, p=p)
            f.insere_fils(0,g)
            f.insere_fils(1,d)
            f.insere_cle(0,tmpCles[p])


    def ajoute(self, x) : 
        ''' ajoute la clé x dans l'arbre (si elle ne s'y trouve pas
        encore '''
        #
        # À COMPLÉTER
        #
        p = self.ordre
        contient, f, i = self.cherche(x)
        if contient: 
            pass
        elif f.nbCles < 2*p :
            f.insere_cle(i,x)
        else:
            self.feuille_scinde(x,f)


    # Barbre a la même hauteur pour tout ces feuilles
    def hauteur(self):
        f = self.racine
        n = 0
        while not f.estFeuille():
            n += 1
            f = f.fils[0]
        return n

    def parcour(self, f=None):
        if f == None: f = self.racine
        nN = 1
        if f.estFeuille(): return nN
        for i in f.fils:
            if i != None:
                nN += self.parcour(i)
        return nN

                




def test_1() :
    ## un B-arbre d'ordre p=1
    f1_1 = Bnoeud([1])
    f1_2 = Bnoeud([3, 4])
    f1_3 = Bnoeud([6])
    racine_1 = Bnoeud([2, 5], [f1_1, f1_2, f1_3])
    A_1 = Barbre(racine_1)
    A_1.dessine("/tmp/petitBarbre1")
    return A_1

def test_2() :
    ## un B-arbre d'ordre p=2
    f2_1 = Bnoeud([1, 2], p=2)
    f2_2 = Bnoeud([4, 5], p=2)
    f2_3 = Bnoeud([7, 8], p=2)
    racine_2 = Bnoeud([3, 6], [f2_1, f2_2, f2_3], p=2)
    A_2 = Barbre(racine_2, p=2)
    A_2.dessine("/tmp/petitBarbre2")
    return A_2

def test(n=50, p=1) :
    A = Barbre(p=p)
    L = list(range(n))
    shuffle(L)
    for i in L : A.ajoute(i)
    A.dessine()
    return L, A




def permutation(n) :
    l = [ (i + 1) for i in range(n) ]
    for i in range(n) :
        r = randint(i, n - 1)
        if i != r :
            l[i], l[r] = l[r], l[i]
    return l

def Barbre_generateur(L,p):
    A = Barbre(p=p)
    for i in L : A.ajoute(i)
    return A

def stat(n,m,p):
    moy = 0
    for i in range(m):
      A = Barbre_generateur(permutation(n),p)
      moy += A.hauteur()
    return moy/m

def tracer(limite,pas,m,p):
    l=[]
    for i in range(1,limite,pas):
        print("Calcul pour p = %d, n = %d"%(i,p))
        l.append(stat(i,m,p))
    return l

def fig_tracer(limite,pas,m,p):
    x = list(range(1,limite,pas))
    y = tracer(limite,pas,m,p)
    plt.plot(x, y, '-.', label='P =%d'%p)
    plt.xlabel('nombre de nœuds')
    plt.ylabel('hauteur moyenne')
    plt.legend(loc='upper left')
    



if __name__ == '__main__':
    # A1 = test_1()
    # A2 = test_2()
    # A2.racine.contient(6)
    # A2.racine.contient(5)
    # A2.cherche(5)
    # A2.cherche(9)
    # test(10)
    # test()
    # test(200, 3)
    # fig_tracer(200,10,10,1)
    # fig_tracer(200,10,10,2)
    # fig_tracer(200,10,10,3)
    # plt.show()
    L = [2, 7, 14, 10, 8, 11, 15, 6, 13, 5, 3, 12, 1, 9, 4]
    print(L)
    A = Barbre_generateur(L,1)
    A.dessine()
    A.parcour()

  
