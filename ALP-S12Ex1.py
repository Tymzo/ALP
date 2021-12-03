# Imports

# Constantes

# Procédures et fonctions
def demande_mot():
    return input("Veuillez entrer un mot: ")



def premier3(mot):
    return mot[ : 3]

def derniers3(mot):
    return mot[(len(mot)-3): ]
    

# Procédure main()
def main():
    # Vos instructions...
    mot = demande_mot()
    print(premier3(mot))
    print(derniers3(mot))
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

