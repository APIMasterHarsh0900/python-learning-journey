My_list= [1,2,3,4,5]
iterator=iter(My_list)
try:
    print(next(iterator))
except StopIteration:
    print("No more elements in the iterator.")

##Concept of Generator##
def my_generator():
    for i in range(3):
        yield i
print(next(my_generator()))

def my_generator1():
    yield 1
    yield 2
    yield 3
gen=my_generator1()
print(next(gen))