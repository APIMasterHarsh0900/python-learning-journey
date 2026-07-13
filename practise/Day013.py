def calculate_bmi(weight, height):
    return weight / (height * height)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

bmi = calculate_bmi(weight, height)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {bmi_category(bmi)}")