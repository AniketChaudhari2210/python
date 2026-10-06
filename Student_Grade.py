students = {
    "Aniket": "A",
    "Rahul": "B",
    "Priya": "A"
}

name = input("Enter student name: ")

if name in students:
    print("Student already exists.")
    grade = input("Enter new grade: ")
    students[name] = grade
    print("Grade updated successfully.")
else:
    grade = input("Enter grade: ")
    students[name] = grade
    print("New student added successfully.")

print("\nAll Student Grades:")
for student, grade in students.items():
    print(student, ":", grade)