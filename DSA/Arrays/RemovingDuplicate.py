def removeDuplicates(nums):
    seen = set()
    dup_count=0
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            dup_count += 1
    return len(nums) - dup_count , list(seen)
print(removeDuplicates([1,2,2,3,3,3,4,5,6])) 

##Solution with Two Pointers approach:
def removeDuplicates(nums):
        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
print(removeDuplicates([1,2,2,3,3,3,4,5,6]))