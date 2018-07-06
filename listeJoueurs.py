import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
paramètre: nomsJoueurs une liste de chaines de caractères
résultat: la liste des joueurs avec un joueur courant mis à 0
"""
    res=[]
    num=1
    for nom in nomsJoueurs:
        elem=Joueur(nom)
        res.append((elem[0],elem[1],num))
        num+=1
    return res

#assert ListeJoueurs(["Hugo","Anne","Huzi","Ken"])==[("Hugo",[],1),("Anne",[],2),("Huzi",[],3),("Ken",[],4)],'PB1'


def ajouterJoueur(joueurs, joueur):
    """
ajoute un nouveau joueur à la fin de la liste
paramètres: joueurs un liste de joueurs
joueur le joueur à ajouter
cette fonction ne retourne rien mais modifie la liste des joueurs
"""
    i=len(joueurs)+1
    elem=Joueur(joueur)
    joueurs.append((elem[0],elem[1],i))



def initAleatoireJoueurCourant(joueurs):
    """
tire au sort le joueur courant
paramètre: joueurs un liste de joueurs
cette fonction ne retourne rien mais modifie la liste des joueurs
"""
    JoueursCourant = random.randint(0, len(joueurs)-1)
    var=joueurs[JoueursCourant]
    while var!=joueurs[0]:
        joueurs.append(joueurs[0])
        del joueurs[0]

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
distribue de manière aléatoire des trésors entre les joueurs.
paramètres: joueurs la liste des joueurs
nbTresors le nombre total de trésors à distribuer (on rappelle
que les trésors sont des entiers de 1 à nbTresors)
nbTresorsMax un entier fixant le nombre maximum de trésor
qu'un joueur aura après la distribution
si ce paramètre vaut 0 on distribue le maximum
de trésor possible
cette fonction ne retourne rien mais modifie la liste des joueurs
"""
    Tresors=[]
    tresParJoueur=0
    for v in range(nbTresors):
        Tresors.append(v+1)
    random.shuffle(Tresors)
    tresParJoueur=nbTresors//len(joueurs)
    while tresParJoueur>nbTresorMax and nbTresorMax!=0:
        tresParJoueur-=1
    for x in range(len(joueurs)):
        while len(joueurs[x][1])<tresParJoueur:
            joueurs[x][1].append(Tresors[0])
            del Tresors[0]


def changerJoueurCourant(joueurs):
    """
passe au joueur suivant (change le joueur courant donc)
paramètres: joueurs la liste des joueurs
cette fonction ne retourne rien mais modifie la liste des joueurs
"""
    joueurs.append(joueurs[0])
    del joueurs[0]


def getNbJoueurs(joueurs):
    """
retourne le nombre de joueurs participant à la partie
paramètre: joueurs la liste des joueurs
résultat: le nombre de joueurs de la partie
"""
    return len(joueurs)

assert getNbJoueurs([("Hugo",[1,2,3,4]),("Anne",[5,6,7,8]),("Huzi",[9,10,11,12]),("Ken",[13,14,15,16])])==4


def getJoueurCourant(joueurs):
    """
retourne le joueur courant
paramètre: joueurs la liste des joueurs
cette fonction ne retourne rien mais modifie la liste des joueurs
"""
    return joueurs[0]

#assert getJoueurCourant([("Hugo",[1,2,3,4]),("Anne",[5,6,7,8]),("Huzi",[9,10,11,12]),("Ken",[13,14,15,16])])==("Hugo",[1,2,3,4]),'PB1'


def joueurCourantTrouveTresor(joueurs):
    """
Met à jour le joueur courant lorsqu'il a trouvé un trésor
c-à-d enlève le trésor de sa liste de trésors à trouver
paramètre: joueurs la liste des joueurs
cette fonction ne retourne rien mais modifie la liste des joueurs
"""
    tresorTrouve(joueurs[0])


def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
retourne le nombre de trésor restant pour le joueur dont le numero
est donné en paramètre
paramètres: joueurs la liste des joueurs
numJoueur le numéro du joueur
résultat: le nombre de trésors que joueur numJoueur doit encore trouver
"""
    return getNbTresorsRestants(joueurs[numJoueur-1])

#assert nbTresorsRestantsJoueur([("Hugo",[1,2,3,4]),("Anne",[7,8]),("Huzi",[9,10,11,12,19]),("Ken",[13,14,15,16,17,18])],3)==6


def numJoueurCourant(joueurs):
    """
retourne le numéro du joueur courant
paramètre: joueurs la liste des joueurs
résultat: le numéro du joueur courant
"""
    return joueurs[0][2]

def nomJoueurCourant(joueurs):
    """
retourne le nom du joueur courant
paramètre: joueurs la liste des joueurs
résultat: le nom du joueur courant
"""
    return joueurs[0][0]

#assert nomJoueurCourant([("Hugo",[1,2,3,4]),("Anne",[5,6,7,8]),("Huzi",[9,10,11,12]),("Ken",[13,14,15,16])])=="Hugo",'PB1'
#assert nomJoueurCourant([("Hugo",[1,2,3,4]),("Anne",[5,6,7,8]),("Huzi",[9,10,11,12]),("Ken",[13,14,15,16])])=="Hugo",'PB1'

def nomJoueur(joueurs,numJoueur):
    """
retourne le nom du joueur dont le numero est donné en paramètre
paramètres: joueurs la liste des joueurs
numJoueur le numéro du joueur
résultat: le nom du joueur numJoueur
"""
    res=None
    for personne in joueurs:
        if personne[-1]==numJoueur:
            res=personne[0]
    return res

#assert nomJoueur([("Hugo",[1,2,3,4]),("Anne",[5,6,7,8]),("Huzi",[9,10,11,12]),("Ken",[13,14,15,16])],2)=="Huzi",'PB1'


def prochainTresorJoueur(joueurs,numJoueur):
    """
retourne le trésor courant du joueur dont le numero est donné en paramètre
paramètres: joueurs la liste des joueurs
numJoueur le numéro du joueur
résultat: le prochain trésor du joueur numJoueur (un entier)
"""
    return prochainTresor(joueurs[numJoueur-1])

#assert prochainTresorJoueur([("Hugo",[1,2,3,4]),("Anne",[5,6,7,8]),("Huzi",[9,10,11,12]),("Ken",[13,14,15,16])],2)==5,'PB1'


def tresorCourant(joueurs):
    """
retourne le trésor courant du joueur courant
paramètre: joueurs la liste des joueurs
résultat: le prochain trésor du joueur courant (un entier)
"""
    return prochainTresor(joueurs[0])

#assert tresorCourant([("Hugo",[1,2,3,4]),("Anne",[5,6,7,8]),("Huzi",[9,10,11,12]),("Ken",[13,14,15,16])])==1,'PB1'


def joueurCourantAFini(joueurs):
    """
indique si le joueur courant a gagné
paramètre: joueurs la liste des joueurs
résultat: un booleen indiquant si le joueur courant a fini
"""
    if getNbTresorsRestants(joueurs[0])==0:
        return True
    else:
        return False

#assert joueurCourantAFini([("Hugo",[1,2,3,4]),("Anne",[5,6,7,8]),("Huzi",[9,10,11,12]),("Ken",[13,14,15,16])])==False,'PB1'
#assert joueurCourantAFini([("Hugo",[]),("Anne",[5,6,7,8]),("Huzi",[9,10,11,12]),("Ken",[13,14,15,16])])==True,'PB1'