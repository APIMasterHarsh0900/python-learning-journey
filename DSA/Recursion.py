def factorial(n):
  if n==0 or n==1:
    return 1
  smallAns = factorial(n-1)
  ans = n * smallAns
  return ans
print(factorial(5))

## Recursion in Python is function calling itself but in its recursion limit to avoid stack overflow error##

import sys
sys.setrecursionlimit(100)

def print_numbers(n):
    if n == 0: ## Base case to stop the recursion call to avoid stack overflow error
        return
    print(n)
    print_numbers(n-1)
print_numbers(5)

"Thus the recurion in problem solving is dividing the problem in smaller portion and then solve the big problem with its smaller parts solutions"

def sum(n):
   if n==1:
       return 1
   smallans=sum(n-1)
   ans=n+smallans
   return ans
print(sum(5))

### Problem to find the number of digits in a number using recursion
def count_digits(n):
   if(n>=1 and n<=9):
       return 1
   smallNum= int(n/10)
   smallans=count_digits(smallNum)
   ans=1+smallans
   return ans
print(count_digits(12345))  
print(count_digits(1234567890))

#### Problem to find the sum of digits in a number using recursion
def sum_of_digits(n):
    if(n>=1 and n<=9):
         return n
    if (n==0):
        return 0
    smallans= sum_of_digits(n//10)
    ans=n%10+smallans
    return ans
print(sum_of_digits(12345))