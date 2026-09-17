#Day 2 of the Interview preparation

My_list=[1,2,3,4,5]
My_list[0]=10
print(My_list)
#List Comprehensions

My_list=[1,2,3,4,5]
square=[num*num for num in My_list]
print(square)
Big_elements=[num for num in My_list if num>3]
print(Big_elements)
even_elements=[num for num in My_list if num%2==0]
print(even_elements)

My_list=[1,2,3,4,5]
square={num:num*num for num in My_list}
print(square)
###
def test(a, *args):
    print(a)
    print(args)

print(test(10, 20, 30, 40))
##Lambda function
addition=lambda a,b:a+b
print(addition(10,20))

##Map function is used to apply a function to all the items in an iterable (like a list) and return a new iterable with the results. It takes two arguments: a function and an iterable.
def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]
result = list(map(square, numbers))
print(result)

numbers = [1, 2, 3, 4, 5]
result= list(map(lambda num:num*num,numbers))
print(result)
##Oops concepts in python
class Employee:

    company = "ABC"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name, self.company)


class Developer(Employee):

    def show(self):
        print(self.name, "Developer", self.company)


e1 = Employee("Harsh")
e2 = Developer("Rahul")

print(e1.show())
print(e2.show())