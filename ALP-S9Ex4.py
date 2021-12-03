# Imports

# Constantes

# Procédures et fonctions

def afficher_liste(ma_liste,ma_liste2,valeur_max,valeur_min):
    for i in ma_liste:
        if i > valeur_min and i < valeur_max:
            ma_liste2.append(i)
            
        
    print("Nombre d'éléments: ",len(ma_liste2))
        
# Procédure main()
def main():
    # Vos instructions...
    ma_liste = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8]
    ma_liste2 = []
    valeur_min = int(input("Entrez une valeur min: "))
    valeur_max = int(input("Entrez une valeur max: "))
    afficher_liste(ma_liste,ma_liste2,valeur_max,valeur_min)
# Appel de la procédure main()
if __name__ == "__main__":
    main()

