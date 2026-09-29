def returntheListofindices(arr,element,index):
    if (len(arr)==index):
        return []
    smalllist=returntheListofindices(arr,element,index+1)
    if (arr[index]==element):
        ans=[index]+smalllist
        return ans
    else:
        return smalllist
print(returntheListofindices([3,3,3,3,3,3,3,3,3,3,3,3],9,0))


def sum_elements(arr):
    if len(arr)==0:
        return 0
    smallans=sum_elements(arr[1:])
    ans=arr[0]+smallans
    return ans
##with simple logic

def sum_elements(arr):
    n=len(arr)
    sum=0
    i=0
    while(i<n):
        sum+=arr[i]
        i+=1
    return sum
print(sum_elements([1,2,3,4,5,6,7,8,9,10]))

def sum_elements(arr):
    n=len(arr)
    total=0
    for element in arr:
        total=total+element
        return total  

    ##Program to count the number of digits in a number  

def count_digits(n):
    if (n==0):
        return 1
    if (n>=1 and n<=9):
        return 1
    smallans=count_digits(n//10)
    ans=1+smallans
    return ans
print(count_digits(1234567890))
### Program to find the maximum element in an array using recursion
def max_element(arr):
    if len(arr)==0:
        return []
    if len(arr)==1:
        return arr[0]
    smallans=max_element(arr[1:])
    if arr[0]>smallans:
        return arr[0]
    else:
        return smallans
print(max_element([1,3,6,9,8]))

###Checking if an element is present in a Array
def check_ele(arr,key):
    if (len(arr)==0):
        return False
    if (len(arr)==1 and key==arr[0]):
        return True
    small_ans= check_ele(arr[1:],key)
    if (arr[0]==key):
        return True
    else:
        return small_ans
print(check_ele([2,5,8,10],3))

    
    