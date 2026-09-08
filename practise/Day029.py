with open('Example.txt','r') as file:
    content = file.read()
    print(content)


import os

path= 'example.txt'
if os.path.isfile(path):
    print(f"The path {path} exists and is a file.")
elif os.path.isdir(path):
    print(f"The path {path} exists and is a directory.")
else:
    print(f"The path {path} does not exist.")