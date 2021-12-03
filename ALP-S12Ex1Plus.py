# Imports

# Constantes

# Procédures et fonctions
def demande_mot():
    return input("Veuillez entrer un mot: ")

def demande_nbCaracteres():
    return int(input("Veuillez entrer un nomvre de caractères: "))

def premier3(mot,caractere):
    return mot[ : caractere]

def derniers3(mot,caractere):
    return mot[(len(mot)-caractere): ]
    

# Procédure main()
def main():
    # Vos instructions...
    mot = demande_mot()
    caractere = demande_nbCaracteres()
    print(premier3(mot,caractere))
    print(derniers3(mot,caractere))
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()


