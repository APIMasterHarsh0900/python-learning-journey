def duplicates(arr):
    n=len(arr)
    for i in range(0,n-1):
        if arr[i]==arr[i+1]:
            return True
    return False
print(duplicates([1,4,3,4,5,6]))

##### This above approach works only for adjacent duplicates elements and it will not work for non-adjacent duplicates. To find duplicates in an array regardless of their position, we can use a set to track seen elements. Here's an improved version of the function:

def duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

print(duplicates([1,4,3,4,5,6]))

##Method 2: using set method it works as set is a collection of only unique elements and its time complexity is o(n).
def duplicates(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                return True
    return False
print(duplicates([1,4,3,4,5,6]))
#Method 3: also works but its time complexity is o(n^2) as it uses nested loops to compare each element with every other element in the array.
