import sys

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True :
    user_choice = input(MENU)
    
    if user_choice not in MENU_CHOICES : 
        print("commande invalide")
        continue
    
    if user_choice == "1" : #ajouter element
        element = input("Ajouter element :")
        LISTE.append(element)
        print(f"element {element} ajouté")
        
    if user_choice == "2" : #retirer element
        element = input("delete element :")
        if element in LISTE :
            LISTE.remove(element)
            print("element enlevé")
        else :
            print("element n'est pas dans la liste")
            
    if user_choice == "3" : # afficher liste
        print(LISTE)
        
    if user_choice == "4" : #vider liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
        
    if user_choice == "5" :
        print("À bientôt !")
        sys.exit()
    
    print("-" * 50)