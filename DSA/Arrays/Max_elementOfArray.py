def max_element(arr):
    if not arr:
        return None  # Return None for empty array

    max_val = arr[0]  # Assume the first element is the maximum
    for num in arr:
        if num > max_val:
            max_val = num  # Update max_val if a larger number is found
    return max_val  # Return the maximum value found
print(max_element([1,3,5,9,7]))