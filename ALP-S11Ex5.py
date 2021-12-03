

# Constantes

DESCENT = 0
MONTER = 1
ESPACE = " "

# Procédures et fonctions
def affiche_en_escalier(mot, sens):
    for i in range(len(mot)):
        if sens == DESCENT :
            print(i*ESPACE + mot[i])
        elif sens == MONTER :
            print(((len(mot)-1)-i)*ESPACE + mot[i])
        
# Procédure main()
def main():
    # Vos instructions...
    demande_mot = str(input("Veuillez entrer un mot: "))
    demande_type_escalier = int(input("Veuillez dire dans quel sens vous voulez partir: (montant = 1 ou descendant = 0) "))
    affiche_en_escalier(demande_mot,demande_type_escalier)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
