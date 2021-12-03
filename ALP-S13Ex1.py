# Imports

# Constantes

# Procédures et fonctions


### SANS  la méthode keys ###
def afficher_cle(dico):
    for cle in dico:
        print(cle)
        
### AVEC  la méthode keys ###
# def afficher_cle(dico):
#     for cle in dico.keys():
#         print(cle)        
        

### SANS la méthode values ###
def afficher_valeurs(dico):
    for cle in dico:
        print(dico[cle])

### AVEC la méthode values ###
# def afficher_valeurs(dico):
#     for cle in dico.values():
#         print(cle)
        
### SANS la méthode items ###
def afficher_cle_valeur(dico):
    for cle in dico:
        print(cle,dico[cle])


### AVEC la méthode items ###
# def afficher_cle_valeur(dico):
#     for cle,valeur in dico.items():
#         print(cle,valeur)                

# Procédure main()
def main():
    # Vos instructions...
    dico = {"nom": "Dupuis", "prenom": "Jacque", "age": 30}
    dico ["prenom"] = "Jacques"
    print(dico)
    afficher_cle(dico)
    afficher_valeurs(dico)
    afficher_cle_valeur(dico)
    print(f"{dico['prenom']} {dico['nom']} a {dico['age']}")
    

# Appel de la procédure main()
if __name__ == "__main__":
    main()

