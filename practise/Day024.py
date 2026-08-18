class Node: # We are creating a class called Node which will represent a single node in a linked list
    def __init__(self, data): # We are craeting a constructor to initialize the data and next pointer of the node
        self.data = data
        self.next = None
first=Node(1) # We are creating a node with data 1 and assigning it to the variable first
second=Node(2) # We are creating a node with data 2 and assigning it to the variable second
third=Node(3) # We are creating a node with data 3 and assigning it to the variable third
fourth=Node(4) # We are creating a node with data 4 and assigning it to the variable fourth
first.next=second # We are linking the first node to the second node by setting the next pointer of the first node to point to the second node
second.next=third # We are linking the second node to the third node by setting the next pointer of the second node to point to the third node
third.next=fourth # We are linking the third node to the fourth node by setting the next pointer of the third node to point to the fourth node
head=first # We are assigning the first node to the variable head
print(head.data) # We are printing the data of the head node which is 1
print(first.data) # We are printing the data of the first node which is 1
print(second.data) # We are printing the data of the second node which is 2
print(third.data) # We are printing the data of the third node which is 3
print(fourth.data) # We are printing the data of the fourth node which is 4
print("User defined linked list is created successfully") # We are printing a message to indicate that the linked list has been created successfully