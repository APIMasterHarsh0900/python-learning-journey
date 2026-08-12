def sum_list(numbers):
    for i in range(0,len(numbers)):
        return sum(numbers)
print(sum_list([1,2,3,4,5]))


def sum_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(sum_list([1, 2, 3, 4, 5]))

def find_largest(numbers):
    largest = numbers[0]
    index = 0

    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
            index = i

    return index
print(find_largest([3, 8, 2, 10, 5]))
def find_largest(numbers):
    largest=numbers[0]
    index=0
    for i in range(0,len(numbers)):
        return max(numbers)

print(find_largest([3,8,2,10,5]))