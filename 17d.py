# Read the number of students and assignments
n, m = map(int, input().split())

# Read students' scores
students = []
for _ in range(n):
    data = input().split()
    initials = data[0]
    scores = list(map(int, data[1:-1]))
    exam_score = int(data[-1])
    # Remove the lowest assignment score
    scores.remove(min(scores))
    total_score = sum(scores) + exam_score
    print(total_score)
    students.append([initials, total_score])

# Get the maximum score among all students
max_score = max(students, key=lambda x: x[1])[1]

# Calculate final score for each student
results = []
for student in students:
    initials, total_score = student
    adjusted_percentage = (total_score / max_score) * 100
    print(adjusted_percentage)
    # Round up to the nearest integer
    final_score = int(adjusted_percentage + 0.5)
    print(final_score)
    # Assign the letter grade
    if final_score >= 90:
        grade = 'A'
    elif final_score >= 80:
        grade = 'B'
    elif final_score >= 70:
        grade = 'C'
    elif final_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    results.append([initials, total_score, final_score, grade])

# Print the results
for r in results:
    print(r[0], r[1], int(r[2]), r[3])
