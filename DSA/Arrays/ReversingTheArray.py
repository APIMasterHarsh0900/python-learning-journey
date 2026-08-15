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