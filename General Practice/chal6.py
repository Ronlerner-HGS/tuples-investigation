def find_highest_average(students_data):
    highest_avg = 0
    top_student = ""
    
    for student, grades in students_data:
        avg = sum(grades) / len(grades)
        print(f"{student}'s average grade: {avg}")
        if avg > highest_avg:
            highest_avg = avg
            top_student = student
    
    return top_student

students = [
    ("Alice", [92, 95, 88]),
    ("Bob", [85, 81, 89]),
    ("Charlie", [90, 92, 94])
]

top_student = find_highest_average(students)
print(f"\nStudent with highest average: {top_student}")