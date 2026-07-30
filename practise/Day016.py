numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Original:", numbers)
print("Squared:", squared_numbers)

number1=[1,2,3,4,5]
number2=[6,7,8,9,10]
summed_numbers = list(map(lambda x, y: x + y, number1, number2))
print("Summed:", summed_numbers)