def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Find the middle
    mid = len(arr) // 2

    # Divide the array into two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the two sorted halves
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left
    result.extend(left[i:])

    # Add remaining elements from right
    result.extend(right[j:])

    return result