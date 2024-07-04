print("Welcome to my tip calculator")
bill = float(input("Quel est la total de la facture $"))
tip = int(input("How much tip would you like give 10, 12 or 15"))
people = int(input("How many people to split the bill"))

tip_as_percent = tip / 100
total_tip_mount = bill * tip_as_percent 
total_bill = bill + total_tip_mount
bill_per_person = total_bill / people
final_mount = "{:2f}".format(bill_per_person)
final_mount = round(bill_per_person, 2)

print(f"Each person shoud pay: ${final_mount}")

