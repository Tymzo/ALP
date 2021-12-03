# Imports

# Constantes

# Procédures et fonctions

def compter_nb_lettre(demande_mot,demande_lettre_a_compter):
    e = 0
    compteur = 0
    
    for e in demande_mot:
        if e == demande_lettre_a_compter:
            compteur += 1
    print(f"La lettre {demande_lettre_a_compter} ce trouve {compteur} fois dans {demande_mot}")
        
        


# Procédure main()
def main():
    # Vos instructions...
    demande_mot = str(input("Veuillez écrire un mot:" ))
    demande_lettre_a_compter = str(input("Veuillez dire quelle lettre vous voulez compter: "))
    compter_nb_lettre(demande_mot,demande_lettre_a_compter)
    
    
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
