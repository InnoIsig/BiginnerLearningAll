print("Bienvenu sur les informations personnels\n")

try:
    height = int(input("Entrez ta taille en cm "))
    weight = int(input("Entrez ton poid en kg "))
except:
    print("Entrez un nombre")
bill = 0

if height >= 120 and weight >= 70:
    print("Tu viens de reussir le test")
    age = int(input("Quel age as-tu ? "))
    if age < 32:
        bill = 10
        print(f"Tu payes $10")
    elif age < 40:
        bill = 20
        print(f"Tu payes $20")
    elif age < 60:
        bill = 30
        print("Tu payes $30")
    else:
        bill = 50
        print("Tu payes $50")

    Add_photo = input("Tu veux ajouté une photo ? Yes ou No ")
    if Add_photo == "Yes":
        bill += 3
    else:
        bill -= 1
    print(f"La facture a payé est : $ {bill}")
    
else:
    print("Le test échoué. Tu dois beaucoup faire le sport")

