number1 = int(input("Enter the first number"))
number2 = int(input("Enter the second number"))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
modulus = number1 % number2
floor_division = number1 // number2
power = number1 ** number2

print("\nCalculator Results")
print(f"{number1} + {number2} = {addition}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} * {number2} = {multiplication}")
print(f"{number1} / {number2} = {division}")
print(f"{number1} % {number2} = {modulus}")
print(f"{number1} // {number2} = {floor_division}")
print(f"{number1} ** {number2} = {power}")