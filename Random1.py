# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

# import random

# random_inside = random.randint(0, 1)

# if random_inside == 1:
#     print("Heads")
# else:
#     print("Tails")



# student_taille = input().split()
# for n in range(0, len(student_taille)):
#     student_taille[n] = int(student_taille[n])

# total_height = 0
# for height in student_taille:
#     total_height += height
# print(f"La tailles des étudiants = {total_height}")

# nombre_etudiant = 0
# for number in student_taille:
#     nombre_etudiant += 1
# print(f"Le nombre des étudiants = {nombre_etudiant}")

# taille_moyenne = round(total_height / nombre_etudiant )
# print(f"La myenne des etudians = {taille_moyenne}")

student_score = input().split()
for n in range(0, len(student_score)):
        student_score[n] = str(student_score[n])

high_score = 0
for score in student_score:
    if score > high_score:
        high_score = score
print(f"Le plus grand point est : {high_score}")

