students = {
    'Alice': [92, 95, 88],
    'Bob': [85, 81, 89],
    'Charlie': [90, 92, 94]
}

for student, grades in students.items():
    average = sum(grades) / len(grades)
    print(f"{student}'s average grade: {average:.2f}")