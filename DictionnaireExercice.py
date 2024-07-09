student_score = {
    "Harry": 81,
    "Innocent": 78,
    "Gedeo": 99,
    "Cynthia": 74,
    "Moise": 62,
    "David": 52,
    "Neema": 78,
    "Bora": 23,
    "Shangwe": 70
}
student_grades = {}
for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grades[student] = "Exceptionnel"
    elif score > 80:
        student_grades[student] = "Grande distinction"
    elif score > 70:
        student_grades[student] = "Dinstinction"
    elif score > 60:
        student_grades[student] = "Satisfaction"
    else:
        student_grades[student] = "Ajourné"

print(student_grades)