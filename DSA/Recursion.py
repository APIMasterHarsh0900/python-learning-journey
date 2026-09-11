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

"Thus the recurion in problem solving is dividing the problem in smaller poration and then solve the big problem with its smaller parts solutions"

