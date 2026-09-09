try:
    num=int(input("Enter a number: "))
    result=11/num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
finally:
    print("Execution completed.")