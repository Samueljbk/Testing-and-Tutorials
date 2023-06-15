# Create a dictionary that represents a student with the keys name, age, course, and grades.
# Assign appropriate values to each key.
# Print the student's name and their average grade (assuming grades is a list of numerical values).

student = {
    "name": "Sam",
    "age": 27,
    "course": "Computer Science",
    "grades": [95, 98, 85, 78],
}

average_grade = sum(student["grades"]) / len(student["grades"])

print(f"{student['name']}'s average grade is: {average_grade}")
