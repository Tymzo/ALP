# Imports

# Constantes

# Procédures et fonctions


### Version avec slicing ###

def premiere_moitie(s):
    return s[ :round(len(s)/2)]
    
def deuxieme_moitie(s):
    return s[round(len(s)/2): ]

def ajoute_au_milieu(s1,s2):
    return premiere_moitie(s1) + s2 + deuxieme_moitie(s1)
        
### Version sans slicing ###

# def premiere_moitie(s):
#     resultat = ""
#     compteur = 0
#     while compteur < len(s)/2:
#         resultat += s[compteur]
#         compteur += 1
#     return resultat
#     
# def deuxieme_moitie(s):
#     resultat = ""
#     compteur = round(len(s)/2)
#     while compteur < len(s):
#         resultat += s[compteur]
#         compteur += 1
#     return resultat
# 
# def ajoute_au_milieu(s1,s2):
#     return premiere_moitie(s1) + s2 + deuxieme_moitie(s1)

# Procédure main()
def main():
    # Vos instructions...
    demande_mot = str(input("Veuillez entrer un mot: "))
    demande_mot_a_ajouter = str(input("Veuillez entrer un mot en MAJUSCULE à mettre en plein milieu du mot précédent: "))
    print(ajoute_au_milieu(demande_mot,demande_mot_a_ajouter))
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
