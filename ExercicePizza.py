print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? Small, Medium, or Large")  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input("Do you want pepperoni? Yes or No ")  # Do you want pepperoni? "Y" or "N"
extra_cheese = input("Do you want extra cheese? Yes or No")  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "Small":
    bill += 15
elif size == "Medium":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Yes":
    if size == "Small":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Yes":
    bill += 1

print(f"Your final bill is: ${bill}.")
