student_name = "Harsh"
student_age = 26

subjects = ["Python", "SQL", "Git", "Algorithms"]

marks = (90, 85, 95, 88)

student = {
    "Name": student_name,
    "Age": student_age,
    "City": "Bangalore",
}

skills = {"Python", "Git", "SQL", "Python"}

print("Student Profile")

print(f"Name: {student_name}")
print(f"Age: {student_age}")

print("\nSubjects:")
print(subjects)

print("\nMarks:")
print(marks)

print("\nStudent Details:")
print(student)

print("\nSkills:")
print(skills)

print("\nAccessing Data")

print(f"First Subject: {subjects[0]}")
print(f"First Mark: {marks[0]}")
print(f"City: {student['City']}")

print("\nData Types")

print(type(subjects))
print(type(marks))
print(type(student))
print(type(skills))