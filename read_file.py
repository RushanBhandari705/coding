#lets create a program that
# 1. Writes a list of student names and their grades to a file named grades.txt
# 2. Reads the grades.txt and calcualtes the average grade.
# 3. Prints the student data and the average grade.


students = [
    ("Rushan", 85),
    ("Alson", 90),
    ("Huba", 78),
    ("Sudip", 92)
]
with open("grades.txt", "w") as file:
    for name, grade in students:
        file.write(f"{name},{grade}\n")

total = 0
count = 0
student_data = []

with open("grades.txt", "r") as file:
    for line in file:
        name, grade = line.strip().split(",")
        grade = int(grade)
        student_data.append((name, grade))
        total += grade
        count += 1

average = total / count if count > 0 else 0

print("Student Grades:")
for name, grade in student_data:
    print(f"{name}: {grade}")

print(f"\nAverage Grade: {average:.2f}")

with open("grades.txt", "a") as file:
    file.write(f"\nAverage Grade: {average:.2f}\n")