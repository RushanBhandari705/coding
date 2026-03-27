students = [("Rushan", 85), ("Aayush", 92), ("Bikash", 78)]

# Sort by marks
sorted_by_marks = sorted(students, key=lambda x: x[1])
print(sorted_by_marks)  
# [('Bikash', 78), ('Rushan', 85), ('Aayush', 92)]

# Sort by name
sorted_by_name = sorted(students, key=lambda x: x[0])
print(sorted_by_name)  
# [('Aayush', 92), ('Bikash', 78), ('Rushan', 85)]