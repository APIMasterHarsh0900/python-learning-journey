def second_large(nums):
    n=len(nums)
    set_nums=set(nums)
    for ele in set_nums:
        if ele==max(set_nums):
            set_nums.remove(ele)
    return max(set_nums) if set_nums else None
print(second_large([10, 5, 8, 10, 3, 8]))
def second_large(nums):
    unique = sorted(set(nums))
    return unique[-2] if len(unique) > 1 else None  
def second_large(nums):
    n=len(nums)
    max_element=0
    for i in range(n):
        for ele in nums:
            if max_element== ele:
                return nums(i-1)    


def second_large(nums):
    largest = float("-inf")
    second_largest = float("-inf")

    for ele in nums:
        if ele > largest:
            second_largest = largest
            largest = ele

        elif ele > second_largest and ele != largest:
            second_largest = ele

    return second_largest
print(second_large([10, 5, 8, 10, 3, 8]))
