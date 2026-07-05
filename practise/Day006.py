number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print(f"{number1} is greater than {number2}")

elif number1 < number2:
    print(f"{number2} is greater than {number1}")

else:
    print("Both numbers are equal.")