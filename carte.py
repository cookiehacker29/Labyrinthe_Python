import random
import copy

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""

"""
bNbEbSbO
"""
listeCartes = ['╬', '╦', '╣', '╗', '╩', '═', '╝', 'Ø', '╠', '╔', '║', 'Ø', '╚', 'Ø', 'Ø', 'Ø']

listeCartesSV = ['╦', '╣', '╗', '╩', '═', '╝', '╠', '╔', '║', '╚']

CarteTest = {'carte': '║', 'tresor': 5, 'pions': [1, 2]}
CarteTest2 = {'carte': '╣', 'tresor': 7, 'pions': [1]}
CarteTest3 = {'carte': '═', 'tresor': 7, 'pions': [3]}
CarteTest4 = {'carte': '╠', 'tresor': 4, 'pions': [4]}

dicType = {'type1': ['╩', '╠', '╦', '╣'], 'type2': ['╚', '╔', '╗', '╝'], 'type3': ['║', '═'], 'type4': ['╬']}

dicMur = {'╬': '0000',
          '╦': '1000',
          '╣': '0100',
          '╗': '1100',
          '╩': '0010',
          '═': '1010',
          '╝': '0110',
          '╠': '0001',
          '╔': '1001',
          '║': '0101',
          '╚': '0011'}

def Carte(nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    carte = None
    if nord and est and sud and ouest:
        carte = '╬'
    elif sud and est and ouest:
        carte = '╦'
    elif ouest and nord and sud:
        carte = '╣'
    elif ouest and sud:
        carte = '╗'
    elif ouest and est and nord:
        carte = '╩'
    elif est and ouest:
        carte = '═'
    elif nord and ouest:
        carte = '╝'
    elif nord and sud and est:
        carte = '╠'
    elif est and sud:
        carte = '╔'
    elif nord and sud:
        carte = '║'
    elif nord and est:
        carte = '╚'
    return {'carte': copy.copy(carte), 'tresor': copy.copy(tresor), 'pions': copy.copy(pions)}

"""
    n
o       e
    s
"""


def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a un ou deux murs
    paramètre: c une carte
    """
    listeValide = ['╬', '╦', '╣', '╗', '╩', '═', '╝', '╠', '╔', '║', '╚']
    if c['carte'] in listeValide:
        res = True
    else:
        res = False
    return res


def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    listeNord = ['╦', '╗', '═', '╔']
    if c['carte'] in listeNord:
        res = True
    else:
        res = False
    return res


def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    listeSud = ['╩', '═', '╝', '╚']
    if c['carte'] in listeSud:
        res = True
    else:
        res = False
    return res


def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    listeEst = ['╣', '╗', '╝', '║']
    if c['carte'] in listeEst:
        res = True
    else:
        res = False
    return res


def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    listeOuest = ['╠', '╔', '║', '╚']
    if c['carte'] in listeOuest:
        res = True
    else:
        res = False
    return res


def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c['pions']


def setListePions(c, listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c['pions'] = listePions
    return


def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c['pions'])


def possedePion(c, pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètre: c une carte
    """
    if pion in c['pions']:
        res = True
    else:
        res = False
    return res


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c['tresor']


def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    c['tresor'] = 0
    return


def mettreTresor(c, tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    Cette fonction modifie la carte mais ne retourne rien
    """
    c['tresor'] = tresor
    return


def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien    
    """
    lsPion = c['pions']
    if pion in lsPion:
        lsPion.remove(pion)
    c['pions']=lsPion

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien    
    """
    lsPion = c['pions']
    if pion not in lsPion:
        lsPion.append(pion)
    lsPion.sort()
    c['pions']=lsPion

def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    r = None
    for key, elem in dicType.items():
        if c['carte'] in elem:
            if elem.index(c['carte']) < len(elem) - 1:
                r = elem[elem.index(c['carte']) + 1]
            else:
                r = elem[0]
    c['carte'] = r
    return r

"""

╩ --> ╠

"""


def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    r = None
    for key, elem in dicType.items():
        if c['carte'] in elem:
            elem = elem[::-1]
            if elem.index(c['carte']) < len(elem) - 1:
                r = elem[elem.index(c['carte']) + 1]
            else:
                r = elem[0]
    c['carte'] = r
    return


def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    r = None
    for key, elem in dicType.items():
        if c['carte'] in elem:
            v = random.randint(0, len(elem) - 1)
            r = elem[v]
    c['carte'] = r
    return


def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    res=''
    for lettre in dicMur[c['carte']]:
        res=lettre+res
    return int(res,2)

"""

╩ --> 0001

"""


def decoderMurs(c, code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    nc = None
    for key, elem in dicMur.items():
        if elem == code:
            nc = key
    c['carte'] = nc
    return


def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    return c['carte']


def passageNord(carte1, carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    IndiceC1 = coderMurs(carte1)
    IndiceC2 = coderMurs(carte2)
    IndiceC1='0'*(4-len(str(IndiceC1)))+str(IndiceC1)
    IndiceC2 = '0' * (4 - len(str(IndiceC2))) + str(IndiceC2)
    if IndiceC1[0]=='0' and IndiceC2[2]=='0': res=True
    else : res=False
    return res

"""
carte2 : '╣' --> 0100
carte1 : '║' --> 0101

res : true
"""


def passageSud(carte1, carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    IndiceC1 = coderMurs(carte1)
    IndiceC2 = coderMurs(carte2)
    IndiceC1='0'*(4-len(str(IndiceC1)))+str(IndiceC1)
    IndiceC2 = '0' * (4 - len(str(IndiceC2))) + str(IndiceC2)
    if IndiceC1[2]=='0' and IndiceC2[0]=='0': res=True
    else : res=False
    return res

"""
carte1 : '╣' --> 0100
carte2 : '║' --> 0101

res : true
"""

def passageOuest(carte1, carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    IndiceC1 = coderMurs(carte1)
    IndiceC2 = coderMurs(carte2)
    IndiceC1='0'*(4-len(str(IndiceC1)))+str(IndiceC1)
    IndiceC2 = '0' * (4 - len(str(IndiceC2))) + str(IndiceC2)
    if IndiceC1[-1]=='0' and IndiceC2[1]=='0': res=True
    else : res=False
    return res

"""
carte1 : '╣' --> 0100
carte2 : '═' --> 1010

═ ╣

res : true
"""

def passageEst(carte1, carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux carte
    résultat un booléen    
    """
    IndiceC1 = coderMurs(carte1)
    IndiceC2 = coderMurs(carte2)
    IndiceC1 = '0' * (4 - len(str(IndiceC1))) + str(IndiceC1)
    IndiceC2 = '0' * (4 - len(str(IndiceC2))) + str(IndiceC2)
    if IndiceC1[1] == '0' and IndiceC2[-1] == '0': res = True
    else: res = False
    return res

"""
carte1 : '╠' --> 0001
carte2 : '═' --> 1010

╠ ═

res : true
"""