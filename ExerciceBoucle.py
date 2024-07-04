# Input a Python list of student heights
student_heights = input("Entrez la taille de chaque éléve").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
for heigt in student_heights:
    total_height += heigt
print(f"Total heigh = {total_height}")

number_of_student = 0
for student in student_heights:
    number_of_student += 1

print(f"Numbers student : {number_of_student}")

average_height = round(total_height / number_of_student)
print(f"Average height : {average_height}")
