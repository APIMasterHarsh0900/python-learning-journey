def searchRange(nums, target):

    # Find first occurrence
    low = 0
    high = len(nums) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            first = mid
            high = mid - 1

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    # Find last occurrence
    low = 0
    high = len(nums) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            last = mid
            low = mid + 1

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return [first, last]

def second_occurrence(nums, target):
    low = 0
    high = len(nums) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            first = mid
            high = mid - 1

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    if first != -1 and first + 1 < len(nums) and nums[first + 1] == target:
        return first + 1

    return -1