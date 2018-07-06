#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------
MatriceTest={'lignes':4, 'colonnes':5, 'matrice':[1,2,3,4,5,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]}

'''
1 2 3 4 5       
4 5 6 7 8 
9 1 2 3 4 
5 6 7 8 9       
'''

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    val = []
    for i in range(nbLignes * nbColonnes):
        val.append(valeurParDefaut)
    return {'lignes':nbLignes, 'colonnes':nbColonnes, 'matrice':val}

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice['lignes']

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice['colonnes']

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice['matrice'][getNbColonnes(matrice)*int(ligne)+int(colonne)]



def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice['matrice'][(matrice['colonnes'] * ligne + colonne)] = valeur

#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    res = getVal(matrice, numLig, 0)
    for j in range(getNbColonnes(matrice) - 1):
        setVal(matrice, numLig, j, getVal(matrice, numLig, j+1))
    setVal(matrice, numLig, getNbLignes(matrice) - 1, nouvelleValeur)
    return res

'''
1 2 3 4 5       
4 5 6 7 8 -->   2 3 4 5 X
9 1 2 3 4 -->   
5 6 7 8 9       
'''


def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res = getVal(matrice, numLig, getNbLignes(matrice))
    for j in range(getNbLignes(matrice) - 1, -1, -1):
        setVal(matrice, numLig, j, getVal(matrice, numLig, j-1))
    setVal(matrice, numLig, 0, nouvelleValeur)
    return res

'''
1 2 3 4 5       
4 5 6 7 8 -->   X 1 2 3 4
9 1 2 3 4 -->   
5 6 7 8 9       
'''

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res = getVal(matrice, 0, numCol)
    for j in range(getNbLignes(matrice)-1):
        setVal(matrice,j,numCol,getVal(matrice, j+1, numCol))
    setVal(matrice, getNbLignes(matrice)-1, numCol, nouvelleValeur)
    return res

'''
1 2 3 4 5       
4 5 6 7 8 -->   4 9 5 X
9 1 2 3 4 -->   
5 6 7 8 9       
'''

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res = getVal(matrice, getNbLignes(matrice)-1, numCol)
    for j in range(getNbLignes(matrice) - 1,-1,-1):
        setVal(matrice, j, numCol, getVal(matrice, j - 1, numCol))
    setVal(matrice, 0, numCol, nouvelleValeur)
    return res


'''
1 2 3 4 5       
4 5 6 7 8 -->  X 5-4 9-5 4+5
9 1 2 3 4 -->   
5 6 7 8 9       
'''