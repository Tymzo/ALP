# Série 10, Exercice 1
# Nom et prénom: ?

''' Un magasin vous mandate pour réaliser un outil de contrôle de stock.
    Vous devez réaliser sa première version en respectant les spécifications fournies en commentaires.
    Une liste stock permet à l'utilisateur d'indiquer les numéros d'article qu'il a dans son stock.
    Une liste catalogue contenant tous les numéros d'article existants.
    Vous devez coder la procédure controler_le_stock qui vérifie le contenu de la liste fourni par l'utilisateur
    et qui affiche un message circonstancié (à l'aide de la procédure afficher_msg déjà faite) selon différents critères. '''

# Constantes
# code_erreur pour la procédure afficher_msg
OK = 0
INCONNU = -20
MULTIPLE = -30
TOTAL = -40

# Procédures et fonctions
# Procédure permettant d'afficher un message selon un code_erreur fourni :
#    - si OK: valeur doit contenir le nombre d'articles, position n'est pas pris en compte
#    - si TOTAL: valeur doit contenir le nombre d'erreurs, position n'est pas pris en compte
#    - si INCONNU ou MULTIPLE: valeur doit contenir le numéro d'article, et position l'indice dans le stock 
# Les 3 paramètres sont des entiers (type = int).
# Ne doit (en principe) pas être modifiée.
def afficher_msg(code_erreur,valeur,position=-1):
    if code_erreur == OK:
        print("Aucune erreur. Il y a ",valeur, " article",sep='',end='')
        if valeur > 1:
            print("s",end='')
        print(" dans le stock.")
    elif code_erreur == TOTAL:
        print("Il y a ",valeur, " erreur",sep='',end='')
        if valeur > 1:
            print("s",end='')
        print(" dans le stock.")
    elif code_erreur == INCONNU or code_erreur == MULTIPLE:
        print("Cellule d'indice ",position,", l'article n°",valeur,sep='',end='')
        if code_erreur == INCONNU:
            print(" est inconnu dans le catalogue !")
        else:
            print(" est répertorié plusieurs fois dans le stock !")   

# Procédure permettant de contrôler le contenu de la liste stock et d'afficher un message (appel de la procédure afficher_msg)
# avec un code correspondant à cette analyse :
# - pour chaque article du stock inconnu dans le catalogue : 
#     Appel afficher_msg avec code_erreur = INCONNU, valeur = n° article, position = indice dans stock
# - pour chaque article apparaissant plusieurs fois dans le stock : 
#     Appel afficher_msg avec code_erreur = MULTIPLE, valeur = n° article, position = indice dans stock
# - à la fin du contrôle, si aucune erreur n'a été détectée :
#     Appel afficher_msg avec code_erreur = OK, valeur = nombre d'articles dans le stock
# - par contre, si une ou plusieurs erreurs ont été détectées :
#     Appel afficher_msg avec code_erreur = TOTAL, valeur = nombre d'erreurs détectées
# Cette procédure reçoit en paramètre:
#    - une liste stock contenant les numéros d'article que l'utilisateur a dans son stock (type = int).
#    - une liste catalogue contenant tous les numéros d'article existant (type = int).
def controler_le_stock(stock,catalogue):
    ''' A COMPLETER'''
    nb_erreur = 0  
    indice = 0
    for e in stock :
        if compter(stock, e) > 1:  
            nb_erreur+=1
            afficher_msg(MULTIPLE,e,indice)
    
        elif e not in catalogue:
            nb_erreur+=1
            afficher_msg(INCONNU,e,indice)
                         
        indice+=1
        
    if nb_erreur >= 1:
        afficher_msg(TOTAL,nb_erreur,e)
    
    if nb_erreur == 0:
            afficher_msg(OK,len(stock),e)
        
        

def compter(stock,numero_article):
    compteur = 0
    for element in stock:
        if element == numero_article:
            compteur += 1
    return compteur
                

                             
# Procédure main()
# Charge le catalogue avec tous les articles existants et contrôle le stock fourni par l'utilisateur.
# Ne doit (en principe) pas être modifiée.
def main():
    stock = list(map(int,input("Entrez une liste d'articles: ").split()))
    catalogue = [11,33,55,77,88,66,44,22,123,234,111,333,555,777,888,666,444,222,1234,2345]    
    controler_le_stock(stock,catalogue)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()