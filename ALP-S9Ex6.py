# Imports

# Constantes
NOTES = [3, 6, 5.5, 4.5, 2.5, 4, 5, 4, 3, 4, 2.5, 4.5, 5, 5, 4, 3]
# Procédures et fonctions
def moyenne_arrondie():
    valeur_notes = 0
    moyenne = 0
    
    for i in NOTES:
        if i in NOTES:
            valeur_notes += i
        moyenne = valeur_notes/len(NOTES)
    print("La moyenne de la classe est de: ", round(moyenne,1))
 
def note_inf():
    notes_inferieur = []
    for i in NOTES:
        if i < 4:
            notes_inferieur.append(i)
    print("les notes inferieurs a 4 sont: ",notes_inferieur)
    print("Le nombre de notes inferieurs à 4 est de:",len(notes_inferieur))
    
def meilleur_note():
    note_num_uno = max(NOTES)
    return note_num_uno


def position(note_num_uno):
    for i in NOTES:
        if note_num_uno == i:
            print ("La meilleure note est en position",NOTES.index(i), "et la note est :" , note_num_uno  )
        
#Deuxieme facon de faire le dernier point:
# def meilleure_notes():
#     note_a = NOTES[0]
#     k = 0
#     for i in NOTES:
#         if i >= note_a:
#             note_a = i
#             k+=1
#     print("la meilleure note de la classe est " + str(note_a))
#     print("la position de la meilleur est note dans la liste est la postion " + str(k -1))            

def pire_note():
    note_a = NOTES[0]
    for i in NOTES:
        if i <= note_a:
            note_a = i
    print("La pire note est: ",note_a)
        
# Procédure main()
def main():
    # Vos instructions...
    moyenne_arrondie()
    note_inf()
    note_num_uno = meilleur_note()
    position(note_num_uno)
    pire_note()
# Appel de la procédure main()
if __name__ == "__main__":
    main()

