#Interview Preparation## Day 1
##Topic: Python data structures##
##List, Tuple, set, Dictionary

#Finding the unique elements in a list using set
numbers=[1,2,2,3,4,4,4,5,5,5]
unique_numbers=set(numbers)
print(unique_numbers)
#Finding the error count using dictionary
error_logs={"404": 10, "500": 5, "403": 2, "404": 3}
print(error_logs["404"])

x=10
def test():
    global x
    print(x)
print(test())

x = 10

def test():
    x = 20
    print(x)

test()

print(x)
print(test())

## Exception Handling
try:
    num1= int(input("Enter the first number:"))
    num2= int(input("Enter the second number:"))
    Divison =num1/num2
    print("The division of two numbers is:",Divison)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please input the valid number.")
finally:
    print("Execution completed and Division operation is done successfully.")
## File handling
with open("app.log","r") as file:
    content=file.read()
    print(content)
## Reading a file line by line
with open("app.log", "r") as file:
    for line in file:
        print(line.strip())

## Counting the Error logs in a file
error_count=0
with open("application.log", "r") as file:
    for line in file:
        if "Error" in line:
            error_count=error_count+1
print("Total error logs found:", error_count)

## Finding a maximum element in a list
numbers = [1, 5, 3, 9, 2]
max_number = max(numbers)
print("The maximum number is:", max_number)

def max_element(lst):
    if not lst:
        return None
    max_num= lst[0]
    for num in lst:
        if num>max_num:
            max_num=num
    return max_num
print(max_element([1, 5, 3, 9, 2]))

with open("app.log", "r") as file:
    for line in file:
        try:
            # Process the line
            process_line(line)

        except ValueError as e:
            print(f"Malformed line skipped: {line.strip()}")
            print(f"Error: {e}")
            continue