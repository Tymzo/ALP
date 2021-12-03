# Imports

# Constantes
RELEVES = [11.8, 14.4, 18.6, 16.5, 11.5, 12.3, 9.1] 
# Procédures et fonctions
def moyenne_temp():
    valeur_liste = 0
    moyenne = 0
    
    for i in RELEVES:
        valeur_liste += i
    moyenne = valeur_liste/len(RELEVES)
    print("La moyenne des temperature est de: ", round(moyenne,1))

def temperature_moins_quinze():
    releves = []
    for i in RELEVES:
        if i < 15:
            releves.append(i)
    print(releves)
    
        
    
# Procédure main()
def main():
    # Vos instructions...
    moyenne_temp()
    temperature_moins_quinze()
    
     
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

