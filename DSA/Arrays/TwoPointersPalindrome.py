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