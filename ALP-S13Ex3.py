# Imports

# Constantes

NOMS = ['Londa','Lenita','Beatrice','Kendrick','Genny','Rolf','Meridith','Hilton','Phylis','Candis','Ron','Lecia','Jacquelyn','Gonzalo','Herlinda','Morgan','Han','Sanjuanita','Allie','Fernande','Anna','Gracia','Lula','Merlyn','Tandy','Adah','Ozella','Laureen','Ricky','Miki']
NB_PLONGEES = [20,120,15,150,5,20,30,60,100,8,20,15,30,79,130,66,24,110,8,23,20,77,60,22,30,80,50,20,10,29]

# Procédures et fonctions
def demande_nom():
    return input("Entrez le nom d'une plongeuse: ")


### Exercice 3.1 ###
def combiner_listes(liste_cles, liste_valeurs):
    dico = {}
    for i in range(len(liste_cles)):
        dico[liste_cles[i]] = liste_valeurs[i]
    return dico

            


### Exercice 3.2 ###
def afficher_resultat(demande,dico):
    if demande in dico:
        print(f"{demande} a éffectuée {dico[demande]} plongées")
    else :
        print("Cette plongueuse n'existe pas")

### Exercice 3.3 ###
def afficher_le_plus_fort(dico):
#     nouveau_dico = {}
#     e = liste_valeurs[0]
#     
#     
#     for e in range(len(liste_cles)):
#         if e >= liste_valeurs[e]:
#             e += liste_valeurs[e]
#     
#             nouveau_dico[liste_cles[e]] = liste_valeurs[e]
#         
#     return nouveau_dico

    dico_val_max = {}
    dico_cle_max = {}
    
    
    for cle in range(len(dico)):
        if dico[cle] > dico_cle_max:
            dico_cle_max = dico[cle]
            dico_val_max = dico[val]
            
        
    return dico_cle_max , dico_val_max


# Procédure main()
def main():
    # Vos instructions...
    demande = demande_nom()
    dico = combiner_listes(NOMS, NB_PLONGEES)
    afficher_resultat(demande,dico)
    dico_cle_max,dico_val_max = afficher_le_plus_fort(dico)
    print(nouveau_dico)
    
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
