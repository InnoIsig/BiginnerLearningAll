print("Bienvenu sur la montagne congolaise")
height = int(input("What is your height in cm ? "))
bill = 0

if height >= 120:
    print("You can ride the rollerDRC")
    age = int(input("What is your age ? "))
    if age < 12:
        bill = 5
        print("child tickets is $5.")
    elif age <= 18:
        bill = 7
        print("Young tickets is $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. have a free ride on us")
    else:
        bill = 12
        print("adult tickets is $12.")
    wants_photo = input("Do you want a picture taken ? Yes or No ")
    if wants_photo == "Yes":
        #add $3 dollars
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride")