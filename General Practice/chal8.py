def find_students_with_highest_average(students_dict):
    highest_avg = 0
    top_students = []
    
    for student, info in students_dict.items():
        avg = sum(info['grades']) / len(info['grades'])
        
        if avg > highest_avg:
            highest_avg = avg
            top_students = [student]
        elif avg == highest_avg:
            top_students.append(student)
    
    return top_students, highest_avg

students = {
    'Alice': {
        'name': 'Alice',
        'age': 20,
        'grades': [92, 95, 88]
    },
    'Bob': {
        'name': 'Bob',
        'age': 21,
        'grades': [85, 92, 88]
    },
    'Charlie': {
        'name': 'Charlie',
        'age': 20,
        'grades': [90, 92, 94]
    }
}

top_students, highest_avg = find_students_with_highest_average(students)
print(f"Students with highest average grade ({highest_avg:.2f}):")
for student in top_students:
    print(f"- {student}")