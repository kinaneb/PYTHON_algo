from tp7_ex1_V2 import *

def testData() :
  ''' tableau des arbres du fichier tp7.py '''
  return [arbreVide,  arbreVideComplet,
          arbreFeuille, arbreFeuilleComplet,
          arbreFilGauche,  arbreFilDroit,
          arbreParfait,
          arbrePlanetes, arbrePlanetesComplet,
          arbreFilsGaucheComplet,
          arbreABR, arbreNABR
  ]






def testResults() :
  return [[estVide, None, [True, True,
                           False, False,
                           False, False,
                           False,
                           False, False,
                           False,
                           False, False]], 
          [etiquette, 1, [None, None,
                          None, None,
                          'b', 'b',
                          'b',
                          'Mars', 'Mars',
                          '5',
                          '6', '6']], 
	  [filsGauche, 0, [None, None,
                           None, 1,
                           1, None,
                           1,
                           1, 1,
                           1,
                           6, 6]],
	  [filsDroit, 1, [None, None,
                          None, None,
                          None, 2,
                          None,
                          3, 3,
                          4,
                          9, 9]], 
	  [pere, 1, [None, None,
                     None, 0,
                     0, 0,
                     0,
                     0, 0,
                     0,
                     3, 3]],
	  [estRacine, 0, [False, False,
                          True, True,
                          True, True,
                          True,
                          True, True,
                          True,
                          False, False]], 
          [estFilsGauche, 1, [False, False,
                              False, True,
                              True, False,
                              True,
                              True, True,
                              True,
                              False, False]], 
          [estFilsDroit, 1, [False, False,
                             False, False,
                             False, True,
                             False,
                             False, False,
                             False,
                             True, True]],
          [estFeuille, 1, [False, False,
                           False, True,
                           False, False,
                           False,
                           False, False,
                           False,
                           False, False]] 
  ]

def testAll() :
  tst = testResults()
  arbres = testData()

  print('Arbres : ')
  for j in range(len(arbres)) :
    print(arbres[j])
    dessineArbreBinaire(arbres[j],"./arb_"+str(j))
 
  for i in range(len(tst)) :
    fname = tst[i][0]
    farg = tst[i][1]
    fres = tst[i][2]
    score = 0
    print('Test %s:' % fname.__name__)
    for j in range(len(arbres)) :
      a = arbres[j]
      print (' - test %d/%d: ' % (j + 1, len(arbres)), end='')
      res = fres[j]
      if (farg == None) :
        res = fname(a)
      else :
        res = fname(a,farg)
      if (res == fres[j]) :
        print(' pass')
        score += 1
      else :
        print(" fail: obtenu ", res, end='')
        print(" <> attendu ", fres[j])
        print("\n arbre: ", a )
        print("\n farg: ", farg)
#        print("\n function: ", fname, a[farg])
    print ('  score %d/%d ' % (score, len(arbres)))
