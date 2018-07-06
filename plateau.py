from matrice import *
from carte import *

def afficheLigneSeparatrice(matrice, tailleCellule=4):
    '''
    Affichage d'une matrice
    fonction annexe pour afficher les lignes séparatrices
    '''
    print()
    for i in range(getNbColonnes(matrice) + 1):
        print('-' * tailleCellule + '+', end='')
    print()


def afficheMatrice(matrice, tailleCellule=4):
    '''
    '''
    nbColonnes = getNbColonnes(matrice)
    nbLignes = getNbLignes(matrice)
    print(' ' * tailleCellule + '|', end='')
    for i in range(nbColonnes):
        print(str(i).center(tailleCellule) + '|', end='')
    afficheLigneSeparatrice(matrice, tailleCellule)
    for i in range(nbLignes):
        print(str(i).rjust(tailleCellule) + '|', end='')
        for j in range(nbColonnes):
            print(str(getVal(matrice, i, j)).rjust(tailleCellule) + '|', end='')
        afficheLigneSeparatrice(matrice, tailleCellule)
    print()


def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    plateau = dict()
    mat = Matrice(7, 7)
    passer = []
    cptJonction=12
    cptAngle=4
    cptTD=0

    ####################### Creation carte fix
    # nord, est, sud, ouest
    setVal(mat, 0, 0, Carte(0, 1, 1, 0))
    setVal(mat, 0, 2, Carte(0, 1, 1, 1))
    setVal(mat, 0, 4, Carte(0, 1, 1, 1))
    setVal(mat, 0, 6, Carte(0, 0, 1, 1))

    setVal(mat, 2, 0, Carte(1, 1, 1, 0))
    setVal(mat, 2, 2, Carte(1, 1, 1, 0))
    setVal(mat, 2, 4, Carte(0, 1, 1, 1))
    setVal(mat, 2, 6, Carte(1, 0, 1, 1))

    setVal(mat, 4, 0, Carte(1, 1, 1, 0))
    setVal(mat, 4, 2, Carte(1, 1, 0, 1))
    setVal(mat, 4, 4, Carte(1, 0, 1, 1))
    setVal(mat, 4, 6, Carte(1, 0, 1, 1))

    setVal(mat, 6, 0, Carte(1, 1, 0, 0))
    setVal(mat, 6, 2, Carte(1, 1, 0, 1))
    setVal(mat, 6, 4, Carte(1, 1, 0, 1))
    setVal(mat, 6, 6, Carte(1, 0, 0, 1))

    ####################### Creation carte aleatoire
    for x in range(7):
        for y in range(7):
            if x%2!=0 or y%2!=0:
                val = random.randint(0, len(listeCartesSV) - 1)

                setVal(mat, x, y, copy.copy(Carte(not murNord({'carte': listeCartesSV[val]}),
                        not murEst({'carte': listeCartesSV[val]}),
                        not murSud({'carte': listeCartesSV[val]}),
                        not murOuest({'carte': listeCartesSV[val]}))))

                if getVal(mat,x,y)['carte'] in dicType['type1']: cptJonction+=1
                elif getVal(mat,x,y)['carte'] in dicType['type2']: cptAngle+=1
                elif getVal(mat,x,y)['carte'] in dicType['type3']: cptTD+=1

                while cptJonction>17 or cptAngle>19 or cptTD>11:
                    val = random.randint(0, len(listeCartesSV) - 1)

                    setVal(mat, x, y, copy.copy(Carte(not murNord({'carte': listeCartesSV[val]}),
                               not murEst({'carte': listeCartesSV[val]}),
                               not murSud({'carte': listeCartesSV[val]}),
                               not murOuest({'carte': listeCartesSV[val]}))))

                    if getVal(mat,x,y)['carte'] not in dicType['type1'] : cptJonction-=1
                    elif getVal(mat,x,y)['carte'] not in dicType['type2'] : cptAngle-=1
                    elif getVal(mat,x,y)['carte'] not in dicType['type3'] : cptTD-=1

    # Jonction==18 Angle==20 TD==12
    ####################### Ajout joueurs
    LsCoint = [(0, 0), (6, 0), (0, 6), (6, 6)]
    for i in range(nbJoueurs):
        save = getVal(mat, LsCoint[i][0], LsCoint[i][1])
        save['pions'] = [i + 1]
        setVal(mat, LsCoint[i][0], LsCoint[i][1], save)

    ####################### Ajout tresors
    xAlea, yAlea = 0, 0
    lsTresor = list(range(1,nbTresors+1))
    indice=0
    for x in range(7):
        for y in range(7):
            if ((x % 2 == 0 and y % 2 == 0) and indice<nbTresors) and (x,y) not in LsCoint:
                save = getVal(mat, x, y)
                save['tresor'] = lsTresor[indice]
                setVal(mat, x, y, save)
                indice+=1
                passer.append((x, y))

    while indice<nbTresors:
        while (xAlea, yAlea) in passer:
            xAlea = random.randint(0, 6)
            yAlea = random.randint(0, 6)
            if (xAlea, yAlea) not in passer:
                save = getVal(mat, xAlea, yAlea)
                save['tresor'] = lsTresor[indice]
                setVal(mat, xAlea, yAlea, save)
                indice+=1
        passer.append((xAlea, yAlea))

    plateau['matrice'] = mat['matrice']
    plateau['lignes']=mat['lignes']
    plateau['colonnes']=mat['colonnes']

    ####################### Ajout carte amovible
    val = random.randint(0, len(listeCartesSV) - 1)
    CA = Carte(not murNord({'carte': listeCartesSV[val]}),
               not murEst({'carte': listeCartesSV[val]}),
               not murSud({'carte': listeCartesSV[val]}),
               not murOuest({'carte': listeCartesSV[val]}))

    if CA['carte'] in dicType['type1']:cptJonction += 1
    elif CA['carte'] in dicType['type2']:cptAngle += 1
    elif CA['carte'] in dicType['type3']:cptTD += 1

    while cptJonction > 17 or cptAngle > 19 or cptTD > 11:
        val = random.randint(0, len(listeCartesSV) - 1)
        CA = Carte(not murNord({'carte': listeCartesSV[val]}),
                   not murEst({'carte': listeCartesSV[val]}),
                   not murSud({'carte': listeCartesSV[val]}),
                   not murOuest({'carte': listeCartesSV[val]}))

        if CA['carte'] not in dicType['type1']:cptJonction -= 1
        elif CA['carte'] not in dicType['type2']:cptAngle -= 1
        elif CA['carte'] not in dicType['type3']:cptTD -= 1

    plateau['CA']=CA
    #print("Jonction : {0}\nAngle : {1}\nTD : {2}".format(cptJonction,cptAngle,cptTD))
    return plateau

"""
1 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0  ---> 1 = joueurs --> 1=(0,0) 2=(6,0) 3=(0,6) 4=(6,6)
0 0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 1
"""

def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    lsCarteAmovible=[]
    for i in range(tresorDebut, nbTresors+tresorDebut):
        val = random.randint(0, len(listeCartesSV) - 1)
        CA = Carte(not murNord({'carte': listeCartesSV[val]}),
                   not murEst({'carte': listeCartesSV[val]}),
                   not murSud({'carte': listeCartesSV[val]}),
                   not murOuest({'carte': listeCartesSV[val]}),i,[])
        lsCarteAmovible.append(CA)
        random.shuffle(lsCarteAmovible)
    return lsCarteAmovible

def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    if getTresor(getVal(plateau,lig,col))==numTresor:
        prendreTresor(getVal(plateau,lig,col))
        return True
    else:
        return False

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    for x in range(0,7):
        for y in range(0,7):
            if getTresor(getVal(plateau,x,y))==numTresor:
                return x,y

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    if possedePion(plateau['CA'], numJoueur):
        return 'CA','CA'
    for x in range(0,7):
        for y in range(0,7):
            if possedePion(getVal(plateau,x,y), numJoueur)==True:
                return x,y


def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    prendrePion(getVal(plateau,lin,col),numJoueur)


def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(getVal(plateau,lin,col),numJoueur)

def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    chemin=[]
    #afficher=''
    res=dict()
    res['matrice']=[]
    for x in range(7):
        for y in range(7):

            N=murNord(getVal(plateau,x,y))
            E=murEst(getVal(plateau,x,y))
            S=murSud(getVal(plateau,x,y))
            O=murOuest(getVal(plateau,x,y))

            tracert=[not N, not E, not S, not O]

            res['matrice'].append(tracert)

    res['lignes']=7
    res['colonnes']=7

    if ligD > 0 or ligA < 0 or colA < 0 or colD < 0 or ligD >= 7 or ligA >=7 or colD>=7 or colA>=7:
        return False

    for x in range(7):
        for y in range(7):
            if x==ligD and y==colD:
                chemin.append((ligD,colD))

            if (x,y) in chemin:
                if x+1 < 7 :
                    if getVal(res, chemin[-1][0], chemin[-1][1])[0] and getVal(res, x+1, y)[2]:
                        chemin.append((x-1,y))

                if x - 1 > -1:
                    if getVal(res, chemin[-1][0], chemin[-1][1])[2] and getVal(res, x-1, y)[0]:
                        chemin.append((x+1,y))

                if y - 1 > -1:
                    if getVal(res, chemin[-1][0], chemin[-1][1])[3] and getVal(res, x, y-1)[1]:
                        chemin.append((x, y-1))

                if y + 1 < 7 :
                    if getVal(res, chemin[-1][0], chemin[-1][1])[1] and getVal(res, x, y+1)[3]:
                        chemin.append((x, y+1))

    if (ligA, colA) in chemin: passer = True
    else : passer = False

    return passer

def accessibleProche(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    if ligD<0 or ligA<0 or colA<0 or colD<0 or ligD>=7 or ligA>=7 or colD>=7 or colA>=7:
        return False
    if ligD==ligA and colD==colA:
        return True
    if ligD==ligA and colD<colA and murEst(getVal(plateau,ligD,colD))==False and murOuest(getVal(plateau,ligA,colA))==False:
        return True
    elif ligD==ligA and colD>colA and murOuest(getVal(plateau,ligD,colD))==False and murEst(getVal(plateau,ligA,colA))==False:
        return True
    elif ligD<ligA and colD==colA and murSud(getVal(plateau,ligD,colD))==False and murNord(getVal(plateau,ligA,colA))==False:
        return True
    elif ligD>ligA and colD==colA and murNord(getVal(plateau,ligD,colD))==False and murSud(getVal(plateau,ligA,colA))==False:
        return True
    else:
        return False

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin,
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    lig = ligD
    col = colD
    res=[(ligD,colD)]
    posEnr=[(ligD,colD)]
    derOp=['aaa','a']
    while res!=[]:
        if (lig==ligA and col==colA):
            return res
        elif ((lig-1,col) not in posEnr and accessibleProche(plateau,lig,col,lig-1,col)==True): #Nord accessible
            lig = lig - 1
            derOp.append('lig-1')
            res.append((lig, col))
            posEnr.append((lig, col))
        elif ((lig+1,col) not in posEnr and accessibleProche(plateau,lig,col,lig+1,col)==True): #Est accessible
            lig = lig + 1
            derOp.append('lig+1')
            res.append((lig, col))
            posEnr.append((lig, col))
        elif ((lig,col-1) not in posEnr and accessibleProche(plateau,lig,col,lig,col-1)==True): #Sud accessible
            col = col - 1
            derOp.append('col-1')
            res.append((lig, col))
            posEnr.append((lig, col))
        elif ((lig,col+1) not in posEnr and accessibleProche(plateau,lig,col,lig,col+1)==True): #Ouest accessible
            col = col + 1
            derOp.append('col+1')
            res.append((lig, col))
            posEnr.append((lig, col))
        else:
            if derOp[len(derOp)-1]=='lig-1':
                    lig=lig+1
            if derOp[len(derOp)-1]=='col+1':
                    col=col-1
            if derOp[len(derOp)-1]=='lig+1':
                    lig=lig-1
            if derOp[len(derOp)-1]=='col-1':
                    col=col+1
            del res[len(res) - 1]
            del derOp[len(derOp)-1]
    return None
