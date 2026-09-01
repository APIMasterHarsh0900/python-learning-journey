class Calculator:
    def __init__(self):
        pass    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
cal1= Calculator()
cal2= Calculator()
print(cal1.add(4,5),cal1.subtract(4,5), cal1.multiply(4,5), cal1.divide(4,5))
print(cal2.add(10,2),cal2.subtract(10,2), cal2.multiply(10,2), cal2.divide(10,2))