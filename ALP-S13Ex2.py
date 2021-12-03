# Imports

# Constantes

# Procédures et fonctions
def demande_fruit():
    return input("Quel fruit voulez-vous? ")

def verification_fruit(fruit, prix, stock):
        if fruit in prix and fruit in stock:
            print('le prix des',fruit, 'est de',prix[fruit],'CHF et on en a',stock[fruit], 'en stock')
        else :
            print("Ce fruit n'est pas dans nos stock")
            

def afficher_valeur_stock(prix,stock):
    for fruit in prix:
        print(fruit, ":", round(prix[fruit] * stock[fruit]), "CHF")

#def afficher_stock(prix, stock, fruit):
    

# Procédure main()
def main():
    # Vos instructions...
    prix = {"bananes": 4, "pommes": 2, "oranges": 1.5, "poires": 3}
    stock = {"bananes": 100, "pommes": 290, "oranges": 50, "poires": 120}
    fruit = demande_fruit()
    verification_fruit(demande_fruit, prix, stock)
    afficher_valeur_stock(prix,stock)
    
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

