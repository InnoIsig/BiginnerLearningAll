print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bienvenu sur ma plate-forme")
print("Il y a un jeu important pour se diversture")

choice1 = input('Choisissez entre. Type "gauche" "droite" \n').lower()
if choice1 == "gauche":
    choice2 = input('Choisissez encore entre ce deux types. "attend" "continuer" \n').lower()
    if choice2 == "attend":
        choice3 = input('Choisissez parmi ces couleurs de portes suivantes "rouge" "jaune" "bleu" \n').lower()
        if choice3 == "rouge":
            print("Il y a le feu dans cette chambre")
        elif choice3 == "jaune":
            print("C'est bien la porte de gagnant")
        elif choice3 == "bleu":
            print("Cette chambre est occupée")
        else:
            print("T'as choissi une porte qui n'existe pas")
    else:
        print("Tu seras attanqué par le lion") 
else:
    print("Il y a aucune autorisation dans cette maison")