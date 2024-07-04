print("She said: \"Hello\" word")
print('She said: "Hello" word')

# name = input("What is your name")
# lenght = len(name)
# print(lenght)

# print(len(input("What is your name")))
# print("Hello:"+ "" +input("What is your name"))
print("Hello"[4])
# nombre1 = input("First number")

# name = len(input("What is your name ?"))
# new_check_name = str(name)
# print("Your name has " + new_check_name + " caracters")
#print("Your name has " + str(name) + " caracters")

#print(type(len(input("What is your name"))))

#Convertion 
# a = 234
# print(a + float("300"))

# two_digit = input()
# first_digit = int(two_digit[0])
# second_digit = int(two_digit[1])

# two_digit = first_digit + second_digit
# print(two_digit)

# year = 2024
# age = int(input("What is your year born"))

# resultat = year - age
# new_resultat = str(resultat)
# print("You have " +new_resultat+ " yeas old")

print(3 * 3 + 3 / 3 - 3)

# 1st input: enter height in meters e.g: 1.65 
#Exercice 6
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_for_int = int(weight)
height_for_float = float(height)

bmi = weight_for_int / height_for_float ** 2
bmi_int = int(bmi)
print(bmi_int)

# There are two variables, a and b from input 
#Exercice 4
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = b
b = a
a = c
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


# Fix the code below 👇 
#Execice 2
print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print("Hello " + "world")
print("New lines can be created with a backslash and n.")

#execice 3
num1 = int(input())
num2 = int(input())

print(num1 * num2)

#Exercice 1
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

#Exercice 5
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = first_digit + second_digit

print(two_digit_number)

#Projet 1
print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)

