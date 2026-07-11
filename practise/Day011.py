def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperature = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(temperature)

print(f"Temperature in Fahrenheit: {fahrenheit}")