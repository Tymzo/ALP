# Imports

# Constantes
L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8] #liste de 10 nombres entiers

L2_STR = ["alice", "bob"] #liste de deux chaînes de caractères 

L1_FLO = [-3.5] #liste de un seul nombre réel 

L0 = [] #liste vide

# Procédures et fonctions
def premier_de_la_liste():
    return L10_INT[0]

def dernier_de_la_liste():
    return L10_INT[-1]

def avant_dernier_de_la_liste():
    return L10_INT[-2]

def nieme_valeur_de_la_liste( n):
    return L10_INT[n]

# Procédure main()
def main():
    # Vos instructions...
    n = int(input("Entrer un chiffre "))
    print(premier_de_la_liste())
    print(dernier_de_la_liste())
    print(avant_dernier_de_la_liste())
    print(nieme_valeur_de_la_liste( n))
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

