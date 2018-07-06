def Joueur(nom):
    """
creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
paramètre: nom une chaine de caractères
retourne le joueur ainsi créé
"""
    return nom,[]

#assert Joueur("Hugo")==("Hugo",[])

def ajouterTresor(joueur,tresor):
    """
ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
paramètres:
joueur le joueur à modifier
tresor un entier strictement positif
la fonction ne retourne rien mais modifie le joueur
"""
    if tresor not in joueur[1]:
        joueur[1].append(tresor)

def prochainTresor(joueur):
    """
retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
paramètre:
joueur le joueur
résultat un entier représentant le trésor ou None
"""
    if joueur[1]==[]:
        return None
    else:
        return joueur[1][0]

#assert prochainTresor(("Hugo",[3,5,6,7]))==3
#assert prochainTresor(("Hugo",[]))==None

def tresorTrouve(joueur):
    """
enleve le premier trésor à trouver car le joueur l'a trouvé
paramètre:
joueur le joueur
la fonction ne retourne rien mais modifie le joueur
"""
    del joueur[1][0]

def getNbTresorsRestants(joueur):
    """
retourne le nombre de trésors qui reste à trouver
paramètre: joueur le joueur
résultat: le nombre de trésors attribués au joueur
"""
    return len(joueur[1])

#assert getNbTresorsRestants(("Hugo",[4,7,3,8,5]))==5

def getNom(joueur):
    """
retourne le nom du joueur
paramètre: joueur le joueur
résultat: le nom du joueur
"""
    return joueur[0]

#assert getNom(("Hugo",[4,7,3,8,5]))=="Hugo"