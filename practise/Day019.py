def binary_search(numbers, key):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == key:
            return mid

        elif numbers[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1