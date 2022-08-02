#!/usr/bin/env python3

from os import system
from random import shuffle
from copy import deepcopy

class Bnoeud :

    # constructeur : le premier paramètre est l'objet à construire;
    # il s'appelle self par convention
    def __init__(self, fils, cles=[], pere=None, p=1) :
        ''' ce constructeur ne fait pas de vérification de cohérence
        (entre p et les nbs de clés et de fils) '''
        self.nbCles = len(cles)
        self.nbFils = 0 if fils == None else len(fils)
        # normalement, nbFils = nbCles+1 (sauf pour les feuilles), mais
        # cela peut momentanément ne pas être le cas au cours d'une opération
        self.cles = cles + [None] * (2*p - self.nbCles)
        #self.fils = None if fils == None else fils + [None] * (2*p +1 - self.nbFils)
        self.fils = fils + [None] * (2*p +1 - self.nbFils)if fils != None else None
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

    def vide_cles(self) :
        self.cles = [None] * (self.nbCles)
        self.nbCles = 0
    
    def vide_fils(self) :
        self.fils = []
        self.nbFils = 0
    
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
        # if self.nbCles >= len(self.cles): return None
        # if i<0 or i>self.nbCles : return None
        self.cles[i:self.nbCles+1] = [x] + self.cles[i:self.nbCles]
        self.nbCles += 1
        return x

    def insere_fils(self, i, noeud) :
        ''' insère un noeud comme fils en position i et met à jour le
        nombre de fils
        (vérifie que le nombre de fils permet l'insertion, 
        mais pas que la position i est adaptée) '''
        # if self.nbFils >= len(self.fils): 
        #    return None
        #if i<0 or i>self.nbFils : 
        #    return None
        self.fils[i:self.nbFils+1] = [noeud] + self.fils[i:self.nbFils]
        self.nbFils += 1
        noeud.pere = self
        return noeud

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

        

    def cherche(self, x) : 
        ''' cherche x dans le sous-arbre de racine self '''
        #
        # À COMPLÉTER
        #
        b, i = self.contient(x)
        if b: return b, self, i
        elif (self.nbFils > i):
            return self.fils[i].cherche(x)
        else: return b, self, i

    def Bnoeud_scinde_F(self, x, g, d, p, iFils) :
        if self.pere != None :
            pere = self.pere
            self.supprime_fils(iFils)
            tmpCles = deepcopy(self.cles)
            tmpFils = deepcopy(self.fils)
            iFils1 = pere.fils.index(self)
            tmpFils.insert(iFils,d)
            tmpFils.insert(iFils,g)
            tmpCles.append(x)
            tmpCles.sort()
            g1 = Bnoeud(cles=tmpCles[0:p], fils=tmpFils[0:p+1], pere=self.pere, p=p)
            d1 = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=tmpFils[p+1:2*p+2], pere=self.pere, p=p)
            if pere.nbFils < 2*p+1 :
                pere.supprime_fils(iFils1)
                pere.insere_fils(iFils1, g1)
                pere.insere_fils(iFils1+1, d1)
                pere.insere_cle(iFils1, tmpCles[p])
            else:
                pere.Bnoeud_scinde_F(tmpCles[p], g1, d1, p, iFils1)
        else:
            self.supprime_fils(iFils)
            tmpCles = deepcopy(self.cles)
            tmpFils = deepcopy(self.fils)
            tmpFils.insert(iFils,d)
            tmpFils.insert(iFils,g)
            self.vide_cles()
            self.vide_fils()
            tmpCles.append(x)
            tmpCles.sort()
            g1 = Bnoeud(cles=tmpCles[0:p], fils=tmpFils[0:p+1], pere=self, p=p)
            d1 = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=tmpFils[p+1:2*p+2], pere=self, p=p)
            self.insere_cle(0,tmpCles[p])
            self.insere_fils(0,g1)
            self.insere_fils(1,d1)


    def feuille_scinde_F(self, x, p):
        if self.pere != None :
            pere = self.pere 
            tmpCles = deepcopy(self.cles)
            tmpFils = deepcopy(self.fils)
            iFils = pere.fils.index(self)
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
                pere.Bnoeud_scinde_F(tmpCles[p], g, d, p, iFils)
        else :
            tmpCles = deepcopy(self.cles)
            tmpFils = deepcopy(self.fils)
            self.vide_cles()
            self.vide_fils()
            tmpCles.append(x)
            tmpCles.sort()
            g = Bnoeud(cles= tmpCles[0:p], fils=None, pere=self, p=p)
            d = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=None, pere=self, p=p)
            self.insere_fils(0,g)
            self.insere_fils(1,d)
            self.insere_cle(0,tmpCles[p])




class Barbre :

    def __init__(self, bnoeud=None, p=1) :
        self.racine = bnoeud if bnoeud != None else Bnoeud(None,p=p)
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
            print(x,'    XXX ,         cles  ',f.cles,f.nbCles, f.nbFils)
            
            print(x,'    XXX ,         cles  ',f.cles,f.nbCles, f.nbFils)
            tmpFils.insert(iFils,d)
            tmpFils.insert(iFils,g)
            tmpCles.append(x)
            tmpCles.sort()
            print(x,'    x ,         tmpCles  ',tmpCles)
            g1 = Bnoeud(cles=tmpCles[0:p], fils=tmpFils[0:p+1], pere=f.pere, p=p)
            d1 = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=tmpFils[p+1:2*p+2], pere=f.pere, p=p)
            if pere.nbFils < 2*p+1 :
                pere.supprime_fils(iFils1)
                pere.insere_fils(iFils1, g1)
                pere.insere_fils(iFils1+1, d1)
                pere.insere_cle(iFils1, tmpCles[p])
                print('  pere cles ', pere.cles)
                #return f
            else:
                print(x,'    x ,         cles////////  ',tmpCles[p],g1.cles,d1.cles, pere.cles)
                self.Bnoeud_scinde(tmpCles[p], g1, d1, pere, iFils1)
        else:
            #print('     Bnoeud_scinde racine ',x, g.cles, d.cles, f.cles if f!=None else None)
            f.supprime_fils(iFils)
            tmpCles = deepcopy(f.cles)
            tmpFils = deepcopy(f.fils)
            tmpFils.insert(iFils,d)
            tmpFils.insert(iFils,g)
            f.vide_cles()
            f.vide_fils()
            tmpCles.append(x)
            tmpCles.sort()
            print('  ** fils list ** ', len(tmpFils) if tmpFils != None else 0)
            g1 = Bnoeud(cles=tmpCles[0:p], fils=tmpFils[0:p+1], pere=f, p=p)
            d1 = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=tmpFils[p+1:2*p+2], pere=f, p=p)
            f.insere_cle(0,tmpCles[p])
            #print(f.cles , '   $$$$$ ')
            f.insere_fils(0,g1)
            f.insere_fils(1,d1)
            print('     Bnoeud_scinde racine after ',x, f.fils[0].cles, f.fils[1].cles, f.cles if f!=None else None)
            #return f

    def feuille_scinde(self,x,f):
        print('     feuille_scinde ',x, f.cles)
        p=self.ordre
        if f.pere != None :
            pere = f.pere 
            tmpCles = deepcopy(f.cles)
            tmpFils = deepcopy(f.fils)
            iFils = pere.fils.index(f)
            tmpCles.append(x)
            tmpCles.sort()
            g = Bnoeud(cles=tmpCles[0:p], fils=None, pere=pere, p=p)
            print('  tmpCles[0:p]   ',tmpCles[0:p])
            d = Bnoeud(cles=tmpCles[p+1:2*p+1], fils=None, pere=pere, p=p)
            print('  tmpCles[p+1:2*p+1]   ',tmpCles[p+1:2*p+1])
            if pere.nbFils < 2*p+1 :
                pere.supprime_fils(iFils)
                pere.insere_fils(iFils, d)
                pere.insere_fils(iFils, g)
                pere.insere_cle(iFils, tmpCles[p])
                #print(' ¨¨¨¨¨¨¨¨  ¨¨¨tmpCles[p]     ', tmpCles[p], '  g ',g .cles, '  d ', d.cles)
                #return f
            else :
                print(' ¨¨¨¨¨¨¨¨  ¨¨¨tmpCles[p]     ', tmpCles[p], '  g ',g .cles, '  d ', d.cles,pere.cles)
                self.Bnoeud_scinde(tmpCles[p], g, d, pere, iFils)
                #return f
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
        b, f, i = self.cherche(x)

        #print ("b = ",b," f = ",f.cles," i =",i, " x = ",x)
        #print("Arbre = Racine = ", self.racine.cles, " fils = ", self.racine.nbFils )
        if b: 
            pass
        elif f.nbCles < 2*p :
            f.insere_cle(i,x)
        else:
            f.feuille_scinde_F(x,p)
            #self.feuille_scinde(x,f)
        

    



def test_1() :
    ## un B-arbre d'ordre p=1
    g_1 = Bnoeud([1])
    g_2 = Bnoeud([3, 4])
    g_3 = Bnoeud([6])
    racine_1 = Bnoeud([2, 5], [g_1, g_2, g_3])
    A_1 = Barbre(racine_1)
    A_1.dessine("/tmp/petitBarbre1")
    return A_1

def test_2() :
    ## un B-arbre d'ordre p=2
    d_1 = Bnoeud([1, 2], p=2)
    d_2 = Bnoeud([4, 5], p=2)
    d_3 = Bnoeud([7, 8], p=2)
    racine_2 = Bnoeud([3, 6], [d_1, d_2, d_3], p=2)
    A_2 = Barbre(racine_2, p=2)
    A_2.dessine("/tmp/petitBarbre2")
    return A_2

def test(n=50, p=1) :
    A = Barbre(p=p)
    L = list(range(n))
    shuffle(L)
    print ("L =",L)
    for e, i in enumerate(L) : 
        A.ajoute(i)
        path = "/tmp/Barbre/"+str(e)
        A.dessine(path)
        
    return L, A


if __name__ == '__main__':
    '''A1 = test_1()
    A2 = test_2()
    A2.racine.contient(6)
    A2.racine.contient(5)
    A2.cherche(5)
    A2.cherche(9)'''
    #test(10)
    # L = [34, 40, 15, 9, 10, 42, 28, 14, 46, 2, 18, 48, 22, 36, 20, 13, 35, 8, 19, 3, 29, 21, 24, 1, 25, 0, 39, 6, 30, 23, 32, 47, 26, 5, 27, 12, 45, 49, 7, 11, 33, 41, 44, 38, 4, 31, 16, 43, 17, 37]
    # A = Barbre(p=1)
    # for e, i in enumerate(L) : 
    #     A.ajoute(i)
    #     path = "/tmp/Barbre/"+str(e)
    #     A.dessine(path)
    #test()
    test(200)
  
