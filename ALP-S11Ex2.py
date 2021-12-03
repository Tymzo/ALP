# Imports

# Constantes
MINUSCULES = "abcdefghijklmnopqrstuvwxyz"
MAJUSCULES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM = "0123456789"

# Procédures et fonctions
def compte_et_affiche_types_de_car(demande_car):
    minuscule = 0
    majuscule = 0
    chiffre = 0
    autre_symbole = 0
    pluriel_minuscule=""
    pluriel_majuscule=""
    pluriel_chiffre=""
    pluriel_symbole=""
    
    for e in demande_car:
        
        if e in MINUSCULES:
            minuscule +=1
            
        elif e in MAJUSCULES:
            majuscule += 1 
        
        elif e in NUM:
            chiffre += 1
        
        else:
            autre_symbole += 1
            
    if minuscule > 1 :
        pluriel_minuscule='s'
            
    if majuscule > 1 :
        pluriel_majuscule='s'
                
    if chiffre > 1 :
        pluriel_chiffre='s'
    
    if autre_symbole > 1 :
        pluriel_symbole='s'
            
    print(f"La chaine contient {minuscule} minuscule{pluriel_minuscule},{majuscule} majuscule{pluriel_majuscule}, {chiffre} chiffre{pluriel_chiffre} et {autre_symbole} autre{pluriel_symbole} symbole{pluriel_symbole}")
    
    
    

# Procédure main()
def main():
    # Vos instructions...
    demande_car = str(input("Veuillez entrez une chaîne de caractère: "))
    compte_et_affiche_types_de_car(demande_car)
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
