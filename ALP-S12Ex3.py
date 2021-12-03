# Imports

# Constantes

# Procédures et fonctions

def demande_mot():
    return input("Quel mot voulez-vous tester? ")


def verifie_mot(mot):
    if mot == mot[ : : -1]:
        print(f"Le mot {mot} est un palindrome")
    else:
        print(f"Le mot {mot} n'est pas un palindrome")


# Procédure main()
def main():
    # Vos instructions...
    mot = demande_mot()
    verifie_mot(mot)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
