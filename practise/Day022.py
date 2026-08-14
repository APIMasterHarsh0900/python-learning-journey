def sum_of_elements(lst):
    n=len(lst)
    for i in range (0,n):
        if i==0:
            total=lst[0]
        else:
            total=total+lst[i]
    return total
print(sum_of_elements([1,2,3,4,5]))