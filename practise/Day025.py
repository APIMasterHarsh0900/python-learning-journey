num = int(input("Enter a number: "))

if num <= 1:
    print("Neither prime nor composite")

else:
    is_composite = False

    for i in range(2, num):
        if num % i == 0:
            is_composite = True
            break

    if is_composite:
        print("Composite number")
    else:
        print("Not a composite number")

def is_composite(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True

    return False


num = int(input("Enter a number: "))

if is_composite(num):
    print("Composite number")
else:
    print("Not a composite number")