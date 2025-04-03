import numpy as np

def find_highest_score(scores_matrix, student_names):
    max_score = np.max(scores_matrix)
    student_idx = np.where(scores_matrix == max_score)[0][0]
    
    return max_score, student_names[student_idx]

student_names = ["Alice", "Bob", "Charlie"]
scores = np.array([
    [85, 92, 88],
    [90, 85, 95],
    [78, 88, 82]
])

highest_score, top_student = find_highest_score(scores, student_names)
print(f"Scores matrix:\n{scores}")
print(f"\nHighest score: {highest_score}")
print(f"Achieved by: {top_student}")