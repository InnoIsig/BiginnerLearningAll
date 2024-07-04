import sys

print("Bienvenu sur ma calculatrice\n")

while True:
    try:
        number1 = int(input("Entrez le premier nombre\n"))
        number2 = int(input("Entrez le deuxieme nombre\n"))
    except:
        print("Entrez le nombre valide")

    MENU = input(""" Choisissez entre :
    1. Addition
    2. Soustraction
    3. Multiplication 
    4. Division
    5. L'exponentiation
    6. Division entière
    7. Quitter
    \n""")


    choix = input('Choisissez entre ces opération. "1" "2" "3" "4" "5" "6" "7" \n')

    if choix == "1":
        resultat = number1 + number2
        print(f"Le resultat est: {resultat}")

    elif choix == "2":
        resultat = number1 + number2
        print(f"Le resultat est: {resultat}")

    elif choix == "3":
        resultat = number1 * number2
        print(f"Le resultat est: {resultat}")

    elif choix == "4":
        if number2 == 0:
            print("Impossible de diviser un nombre par zero")
        else:
            resultat = number1 / number2
            resultat_arondir = round(resultat, 2)
            #resultat = "{:2f}".format(resultat)
            print(f"Le resultat est: {resultat_arondir}")
    elif choix == "5":
        resultat = number1 ** number2
        print(f"Le resultat est: {resultat}")

    elif choix == "6":
        resultat = number1 // number2
        print(f"Le resultat est: {resultat}")
        
    elif choix == "7":
        print("Merci d'utiliser cette plate-forme")
        sys.exit()
        
    else:
        print("Choix invalide")


