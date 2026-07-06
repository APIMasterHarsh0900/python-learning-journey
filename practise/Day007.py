student_name = input("Enter student's name: ")
marks = float(input("Enter marks (out of 100): "))

print("\nResult")

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print(f"Student Name : {student_name}")
print(f"Marks        : {marks}")
print(f"Grade        : {grade}")