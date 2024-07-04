print("Bienvenu dans l'appliction de la feacturation\n")

facture = float(input("Quel est le montant du produit acheté? $"))
reduction_produit = int(input("Quel type de reduction as-tu besoin de faire ? de 2, 5, ou 10 "))
people = int(input("Combien de client ont achetés le produit ? "))

total_reduction = reduction_produit / 100
Montant_Preduction = facture * total_reduction
Montant_payer = facture + Montant_Preduction 
Nombre_population = Montant_payer / people
Montant_final = round(Nombre_population, 2)
Montant_final = "{:.2f}".format(Nombre_population)

print(f"Chaque personne doit payer : {Montant_final} dollars")