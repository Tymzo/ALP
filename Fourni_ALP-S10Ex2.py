# Série 10, Exercice 2
# Nom et prénom: ?

''' L'ESIG vous mandate pour réaliser un outil de gestion des notes d’étudiants.
    Vous devez réaliser sa première version en respectant les spécifications fournies.
    L’outil permet de travailler sur les résultats obtenus lors d’une épreuve par une classe d’étudiants.
    Une structure de données permet de stocker des notes. Les notes sont considérées comme des valeurs entières.
    La valeur 0 signifie qu'il n'y a pas de note pour cet étudiant.
    Pour la version suisse, les notes vont de 1 à 6, avec la limite du suffisant à 4.
    (Il est prévu d'en faire par la suite une version pour la France, où les notes vont de 0 à 20, avec la limite du suffisant à 10.) '''

# Constantes
NOTE_OK = 0
AUCUNE_NOTE = 1
NOTE_INVALIDE = -2
QUE_DES_INSUFFISANTS = -3
NOTE_MIN = 1
NOTE_MAX = 6
LIMITE_SUFFISANT = 4

# Procédures et fonctions
# Fonction à résulat entier (type = int) permettant d'analyser les notes fournies en paramètre (des entiers) et de retourner un code correspondant à cette analyse:
#    - si aucune note n’est présente dans la structure (que des 0) :                            retourne AUCUNE_NOTE
#    - s'il y a une note (ou plus) qui n’est pas comprise entre 1 et 6 inclus :                 retourne NOTE_INVALIDE
#    - si toutes les notes sont strictement inférieures à 4 :                                   retourne QUE_DES_INSUFFISANTS
#    - dans tous les autres cas: (toutes les notes sont valides et il y a des notes >= 4) :     retourne NOTE_OK
# Cette procédure reçoit en paramètre:
#    - une liste lst_notes contenant les notes de chaque étudiant (type = int).
def analyse_des_notes(lst_notes):

# # # Méthode 1 avec des fonctions
#     if aucune_note(lst_notes):
#         return AUCUNE_NOTE
#     if note_invalide(lst_notes):
#         return NOTE_INVALIDE
#     if que_des_insuffisants(lst_notes):
#         return QUE_DES_INSUFFISANTS
#     return NOTE_OK
# 
# def que_des_insuffisants(lst_notes):
#     for n in lst_notes:
#         if n >= LIMITE_SUFFISANT:
#             return False
#     return True
# 
# def aucune_note(lst_notes):
#     for note in lst_notes:
#         if note != 0:
#             return False
#     return True
# 
# def note_invalide(lst_notes):
#     for n in lst_notes:
#         if n == 0:
#             pass
#         elif n < NOTE_MIN or n > NOTE_MAX:
#             return True
#     return False

# # # Méthode 2

    compteur = 0

    for e in lst_notes:
        if e == 0:
            compteur +=1
        
        if compteur == len(lst_notes):
            return AUCUNE_NOTE
        
    for e in lst_notes:
        if (e < NOTE_MIN or e > NOTE_MAX) and e != 0:
            return NOTE_INVALIDE
        
    compteur +=1
    
    for e in lst_notes:
        if e < LIMITE_SUFFISANT:
            compteur += 1
        if compteur  == len(lst_notes):
            return QUE_DES_INSUFFISANTS
    return NOTE_OK


# Procédure permettant d'afficher la statistique des notes, c’est-à-dire le nombre d’apparitions de chaque note (6,5,4,3,2,1) fournies en paramètre.
# Cette procédure reçoit en paramètre:
#    - une liste lst_notes contenant les notes de chaque étudiant (type = int).
# Exemple :
#    Nombre de 6 : 3
#    Nombre de 5 : 2
#    Nombre de 4 : 3
#    Nombre de 3 : 0
#    Nombre de 2 : 1
#    Nombre de 1 : 0
def afficher_statistique(lst_notes):
    for note in range(NOTE_MAX,NOTE_MIN -1,-1):
        afficher_statistique_note(lst_notes, note)
        
    
def afficher_statistique_note(lst_notes,note):
    nb = 0
    for n in lst_notes:
        if n == note:
            nb +=1
    print("Nombre de",note,":", nb)
    
    

# Procédure main()
# Test des procédures à développer. Ne doit (en principe) pas être modifiée.
def main():
    lst_notes = list(map(int,input("Entrez une liste de notes").split()))
    code = analyse_des_notes(lst_notes)
    if code == NOTE_OK:
        print("Les notes sont correctes.")
    elif code == AUCUNE_NOTE:
        print("Aucune note !")
    elif code == NOTE_INVALIDE:
        print("Les notes ne sont pas toutes valides !")
    else:
        print("Il n'y a que des insuffisants !")
    print("Statistique :")
    afficher_statistique(lst_notes)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()