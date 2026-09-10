def is_pallindrome(lst):
    n=len(lst)
    i=0
    j=n-1
    while i<j:
        if lst[i]!=lst[j]:
            return False
        i=i+1
        j=j-1
    return True
print(is_pallindrome([1,2,3,2,1]))

def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    
    n=len(lst)
    i=0
    j=n-1
    while i<j:
        lst[i],lst[j]=lst[j],lst[i]
        i=i+1
        j=j-1
    return lst
print(reverse_list([1,2,3,4,5]))

def is_palindrome(s):
    s = s.lower()

    new_s = ""

    for char in s:
        if char.isalnum():
            new_s += char

    i = 0
    j = len(new_s) - 1

    while i < j:
        if new_s[i] != new_s[j]:
            return False

        i += 1
        j -= 1

    return True