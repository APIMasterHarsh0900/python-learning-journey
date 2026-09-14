def count_digits(n):
   if(n>=1 and n<=9):
       return 1
   smallNum= int(n/10)
   smallans=count_digits(smallNum)
   ans=1+smallans
   return ans
print(count_digits(12345))  
print(count_digits(1234567890))