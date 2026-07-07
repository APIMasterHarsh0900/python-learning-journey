def square(num):
    return num * num
result = square(5)
print(result)

def max(a, b):
    if a > b:
        return a
    else:
        return b

max_result = max(10, 20)
print(max_result)

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

even_odd_result = even_or_odd(7)
print(even_odd_result)

def area_Rectangle(length, width):
    return length * width

area_result = area_Rectangle(10, 20)
print(area_result)

def total_marks(Maths, Science, English):
    return Maths + Science + English
def average_marks(Maths, Science, English):
    total = total_marks(Maths, Science, English)
    return total / 3

average_result = average_marks(80, 90, 70)
print(average_result)

def total_marks(maths, science, english):
    return maths + science + english

def average_marks(maths, science, english):
    total = total_marks(maths, science, english)
    return total / 3

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = total_marks(maths, science, english)
average = average_marks(maths, science, english)

print(f"Total Marks = {total}")
print(f"Average Marks = {average}")

def agv_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
print(f"Grade = {agv_grade(average)}")
if average >= 40:
     print("Status = PASS")
else:
     print("Status = FAIL")