def two_sum(arr,target):
    n=len(arr)
    i=0
    j=n-1
    while i<=j:
        if arr[i] +arr[j]== target:
            return [i,j]
        elif arr[i] +arr[j]< target:
            i+=1
        else:
            j-=1
    return None
print(two_sum([3,4,5,7],7))

def two_sum(arr,target):
    n=len(arr)
    i=0
    j=n-1
    while i<=j:
        if arr[i] +arr[j]== target:
            return [i,j]
        else:
            return f"Target sum not found in the array "
    i=i+1
    j=j-1
    return None
print(two_sum([3,4,5,7],7))


def two_sum(arr, target):

    # Store value and original index
    pairs = [(value, index) for index, value in enumerate(arr)]

    # Sort by value
    pairs.sort()

    left = 0
    right = len(pairs) - 1

    while left < right:

        left_value, left_index = pairs[left]
        right_value, right_index = pairs[right]

        current_sum = left_value + right_value

        if current_sum == target:
            return [left_index, right_index]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return None


print(two_sum([7, 3, 5, 1], 8))