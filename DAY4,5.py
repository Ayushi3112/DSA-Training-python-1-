'''
# bubble sort:
#Ascending order:
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":

    arr = [6, 23, 2, 4, 1, 8, 56, 3]

    bubbleSort(arr)

    print(*arr)
'''
'''
# descending order
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":

    arr = [6, 23, 2, 4, 1, 8, 56, 3]

    bubbleSort(arr)

    print(*arr)
'''
'''
#selection sort

# ascending order
def selectionSort(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        for j in range(i+1, len(arr)):
            if min>arr[j]:
                min=arr[j]
                loc=j
                arr[i], arr[loc] = arr[loc], arr[i]
 
if __name__ == "__main__":

    arr = [6, 23, 2, 4, 1, 8, 56, 3]

    selectionSort(arr)

    print(*arr)
'''
'''
#descending order
def selectionSort(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        for j in range(i+1, len(arr)):
            if min<arr[j]:
                min=arr[j]
                loc=j
                arr[i], arr[loc] = arr[loc], arr[i]
 
if __name__ == "__main__":

    arr = [6, 23, 2, 4, 1, 8, 56, 3]

    selectionSort(arr)

    print(*arr)
'''
'''
# insertion sort
# ascending order
def insertionSort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        pos=i
        while current<arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
            arr[pos]=current
        print(arr)
if __name__ == "__main__":

    arr = [5, 43, 2, 4, 1, 7, 26, 3]

    insertionSort(arr)

    print(*arr)
'''
'''
# descending order
def insertionSort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        pos=i
        while current>arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
            arr[pos]=current
        print(arr)
if __name__ == "__main__":

    arr = [5, 43, 2, 4, 1, 7, 26, 3]

    insertionSort(arr)

    print(*arr)
'''
'''
# class in python
class Student:
    def show(self):
        print("I am in show")
 
s=Student();
s.show();
#Constructor:

class Student:
    def __init__(self):
        print("Default constructor")
 
    def show(self):
        print("I am in show")
 
s=Student();
s.show();
'''
'''
#stacks
# stack in python
import sys
class Stacks:
    def push(self):
        pass
    def pop(self):
        pass
    def traverse(self):
        pass
    def peek(self):
        pass
if __name__ == "__main__":
  obj=Stacks()
  while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Traverse")
    print("0. Exit")
    ch=int(input("select any choice"))
    if ch==1:
        obj.push()
    elif ch==2:
        obj.pop()
    elif ch==3:
        obj.traverse()
    elif ch==4:
        obj.peek()
    elif ch==0:
        sys.exit(0)
'''
'''
import sys

class Stacks:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5
    def isFull(self):
        if self.top==self.CAPACITY-1:
            return True
        else:
            return False
    def push(self,ele):
        if self.isFull():
            print("stack is full ")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele, "is pushed")
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
        pass
    def pop(self):
        pass
    def peek(self):
        pass
if __name__ == "__main__":
  obj=Stacks()
  while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Traverse")
    print("0. Exit")
    ch=int(input("select any choice"))
    if ch==1:
        ele=int(input("Enter data: "))
        obj.push(ele)
    elif ch==2:
        obj.pop()
    elif ch==3:
        obj.traverse()
    elif ch==4:
        obj.peek()
    elif ch==0:
        sys.exit(0)
'''
'''
import sys

class Stacks:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5
    def isFull(self):
        if self.top==self.CAPACITY-1:
            return True
        else:
            return False
    def push(self,ele):
        if self.isFull():
            print("stack is full ")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele, "is pushed")
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            ele=self.stack[self.top]
            self.stack.pop()
            self.top=-1
        return ele
    def peek(self):
        pass
if __name__ == "__main__":
  obj=Stacks()
  while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Traverse")
    print("0. Exit")
    ch=int(input("select any choice"))
    if ch==1:
        ele=int(input("Enter data: "))
        obj.push(ele)
    elif ch==2:
        obj.pop()
    elif ch==3:
        obj.traverse()
    elif ch==4:
        obj.peek()
    elif ch==0:
        sys.exit(0)
'''
'''
# Reverse Array Using Stack

class Stacks:

    def __init__(self):
        self.stack = []
        self.top = -1

    # Push element
    def push(self, ele):
        self.top += 1
        self.stack.append(ele)

    # Check empty
    def isEmpty(self):
        return self.top == -1

    # Pop element
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
            return ele


# Main Program
if __name__ == "__main__":

    obj = Stacks()

    arr = [10, 20, 30, 40, 50]

    for i in range(len(arr)):
        obj.push(arr[i])

    rev = []
    for i in range(len(arr)):
        obj.pop()
        rev.append(obj.pop())

    print(rev)
'''
'''
import sys
class Queue:
    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0
        self.CAPACITY = 5

    # Check queue is full
    def isFull(self):
        if self.rear == self.CAPACITY - 1:
            return True
        else:
            return False

    # Check queue is empty
    def isEmpty(self):
        if self.front > self.rear:
            return True
        else:
            return False

    # Insert element
    def enqueue(self, ele):
        if self.isFull():
            print("Queue is full")
        else:
            self.rear = self.rear + 1
            self.queue.append(ele)   # corrected
            print(ele, "is inserted")   # corrected

    # Display elements
    def traverse(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements are:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])

    # Delete element
    def dequeue(self):
      pass

    # Show front element
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front element is:", self.queue[self.front])


if __name__ == "__main__":

    obj = Queue()

    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        ch = int(input("Select any choice: "))

        if ch == 1:
            ele = int(input("Enter data: "))
            obj.enqueue(ele)

        elif ch == 2:
            obj.dequeue()

        elif ch == 3:
            obj.peek()          

        elif ch == 4:
            obj.traverse()      

        elif ch == 0:
            sys.exit(0)

        else:
            print("Invalid choice")
'''
'''
# Reverse Queue using Stack

# Queue Class
import sys

class Queue:

    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0
        self.CAPACITY = 5

    # Check queue is full
    def isFull(self):
        return self.rear == self.CAPACITY - 1

    # Check queue is empty
    def isEmpty(self):
        return self.rear == -1

    # Insert element
    def enqueue(self, ele):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear += 1
            self.queue.append(ele)
            print(ele, "is inserted")

    # Delete element
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        else:
            ele = self.queue.pop(0)
            self.rear -= 1

            if self.rear == -1:
                self.front = 0

            return ele

    # Display queue
    def traverse(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue Elements:")
            for i in self.queue:
                print(i)

    # Peek element
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front Element:", self.queue[0])


# Main Program

if __name__ == "__main__":

    q = Queue()

    while True:

        print("\n1.Enqueue")
        print("2.Dequeue")
        print("3.Traverse")
        print("4.Peek")
        print("5.Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            ele = int(input("Enter element: "))
            q.enqueue(ele)

        elif ch == 2:
            ele = q.dequeue()

            if ele != None:
                print(ele, "is deleted")

        elif ch == 3:
            q.traverse()

        elif ch == 4:
            q.peek()

        elif ch == 5:
            sys.exit()

        else:
            print("Invalid Choice")
'''
'''
import sys

# Queue Class
class Queue:

    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0
        self.CAPACITY = 5

    # Check queue is full
    def isFull(self):
        return self.rear == self.CAPACITY - 1

    # Check queue is empty
    def isEmpty(self):
        return self.rear == -1

    # Insert element
    def enqueue(self, ele):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear += 1
            self.queue.append(ele)

    # Delete element
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        else:
            ele = self.queue.pop(0)
            self.rear -= 1
            return ele

    # Display queue
    def traverse(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            for i in self.queue:
                print(i, end=" ")
            print()


# Stack Class
class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1

    # Push element
    def push(self, ele):
        self.top += 1
        self.stack.append(ele)

    # Check empty
    def isEmpty(self):
        return self.top == -1

    # Pop element
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            ele = self.stack.pop()
            self.top -= 1
            return ele


# Main Function
if __name__ == "__main__":

    obj1 = Queue()
    obj2 = Stack()

    # Insert elements into Queue
    for i in range(obj1.CAPACITY):
        ele = int(input("Enter element: "))
        obj1.enqueue(ele)

    print("\nOriginal Queue:")
    obj1.traverse()

    # Step 1: Queue -> Stack
    for i in range(obj1.CAPACITY):
        ele = obj1.dequeue()
        obj2.push(ele)

    # Step 2: Stack -> Queue
    for i in range(obj1.CAPACITY):
        ele = obj2.pop()
        obj1.enqueue(ele)

    print("\nReversed Queue:")
    obj1.traverse()
'''
'''
# insert element in the array

arr = []
n = int(input("Enter size: "))
for i in range(n):
    arr.append(int(input("Enter no: ")))
key = int(input("Enter key element which is to be insert: "))
loc = int(input("Enter location: "))
arr.append(0)

for i in range(len(arr) - 1, loc, -1):
    arr[i] = arr[i - 1]
arr[loc] = key

print("Array after insertion:")
print(arr)
'''
'''
# delete key element from the array
arr = []
n = int(input("Enter size: "))
for i in range(n):
    arr.append(int(input("Enter no: ")))
key = int(input("Enter key element which is to be delete: "))

for i in range(len(arr)):
    if arr[i] == key:
        for j in range(i, len(arr) - 1):
            arr[j] = arr[j + 1]
        arr.pop()
        break
print("Array after deletion:")
print(arr)
'''
'''
# rotate an array to the right

arr = []
n = int(input("Enter size: "))
for i in range(n):
    arr.append(int(input("Enter no: ")))
step = int(input("Enter number of rotations: "))

for i in range(step):
    loc = len(arr) - 1
    temp = arr[loc]
    arr.append(0)
    for j in range(len(arr) - 1, 0, -1):
        arr[j] = arr[j - 1]
    arr[0] = temp
    arr.pop()
print("Array after right rotation:")
print(arr)
'''
'''
# intersection of two arrays

arr1 = []

n1 = int(input("Enter size of first array: "))

for i in range(n1):
    arr1.append(int(input("Enter no: ")))

arr2 = []

n2 = int(input("Enter size of second array: "))

for i in range(n2):
    arr2.append(int(input("Enter no: ")))

arr3 = []

for i in range(len(arr1)):

    temp = arr1[i]

    # Check duplicate in result array
    flag = 0

    for k in range(len(arr3)):
        if temp == arr3[k]:
            flag = 1
            break

    if flag == 0:

        for j in range(len(arr2)):

            if temp == arr2[j]:

                arr3.append(temp)
                break

print("Intersection of arrays:")
print(arr3)
'''
'''
# Rearrange Positive and Negative Number
arr = [-1, 2, -3, 4, 5, -6]
pos = []
neg = []
for i in arr:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
result = []
for i in range(len(neg)):
    result.append(neg[i])
    result.append(pos[i])
if len(pos) > len(neg):
    result.append(pos[-1])

print(result)
'''
'''
# Reverse the string without inbuilt function
s = ["hello"]
word = s[0]
rev = ""
for i in range(len(word) - 1, -1, -1):
    rev = rev + word[i]
print("Original String:",s)
print("Reversed String:", rev)
'''
'''
s="ayushi"
rev=""
for x in s:
    rev=x+rev
print(rev)
'''
'''
# check for a valid palindromic string
s = "A man, a plan, a canal: Panama"
str = ""
for i in s:
    if i.isalpha():
        str = str + i.lower()
rev = ""
for i in range(len(str)-1, -1, -1):
    rev = rev + str[i]
if str == rev:
    print("Valid Palindrome")
else:
    print("Invalid Palindrome")
'''
'''
# check for valid anagram string
s1 = "listen"
s2 = "silent"
str1 = ""
str2 = ""
for i in s1:
    if i.isalpha():
        str1 = str1 + i.lower()
for i in s2:
    if i.isalpha():
        str2 = str2 + i.lower()
a = sorted(str1)
b = sorted(str2)
if a == b:
    print("Anagram")
else:
    print("Not Anagram")
'''
'''
#inbuilt function:
# check for valid anagram string
s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
'''
'''
import sys

class GetNode:

    def __init__(self):   
        self.data = None
        self.next = None


class Linkedlist:

    def __init__(self):   
        self.head = None

    def append(self):

        data = int(input("Enter data: "))

        newNode = GetNode()

        newNode.data = data

        if self.head == None:
            self.head = newNode

        else:
            ptr = self.head

            while ptr.next != None:
                ptr = ptr.next

            ptr.next = newNode   

        print(data, "is added")

    def traverse(self):

        if self.head == None:
            print("Linked List not Present")

        else:
            ptr = self.head

            while ptr != None:
                print(ptr.data, " -> ", end="")

                ptr = ptr.next


if __name__ == '__main__':

    obj = Linkedlist()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()

        elif n == 2:
            obj.traverse()

        elif n == 0:
            sys.exit(0)
'''
'''
import sys

class GetNode:

    def __init__(self):
        self.data = None
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    # Append at end
    def append(self):

        data = int(input("Enter data: "))

        newNode = GetNode()

        newNode.data = data

        if self.head == None:
            self.head = newNode

        else:
            ptr = self.head

            while ptr.next != None:
                ptr = ptr.next

            ptr.next = newNode

        print(data, "is added")

    # Traverse
    def traverse(self):

        if self.head == None:
            print("Linked List not Present")

        else:
            ptr = self.head

            while ptr != None:
                print(ptr.data, " -> ", end="")

                ptr = ptr.next

            print("None")

    # Add at beginning
    def addatbefore(self):

        data = int(input("Enter data: "))

        newNode = GetNode()

        newNode.data = data

        newNode.next = self.head

        self.head = newNode

        print(data, "is added at beginning")

    # Delete at beginning
    def deltatbeg(self):

        if self.head == None:
            print("Linked List Empty")

        else:
            temp = self.head.data

            self.head = self.head.next

            print(temp, "is deleted")

    # Delete at end
    def deltatend(self):

        if self.head == None:
            print("Linked List Empty")

        elif self.head.next == None:

            temp = self.head.data

            self.head = None

            print(temp, "is deleted")

        else:

            ptr1 = self.head
            ptr2 = self.head.next

            while ptr2.next != None:

                ptr1 = ptr2
                ptr2 = ptr2.next

            ptr1.next = None

            print(ptr2.data, "is deleted")

    # Delete at key
    def deltatkey(self):

        key = int(input("Enter key to delete: "))

        if self.head == None:
            print("Linked List Empty")

        elif self.head.data == key:

            self.head = self.head.next

            print(key, "is deleted")

        else:

            ptr1 = self.head
            ptr2 = self.head.next

            while ptr2 != None:

                if ptr2.data == key:

                    ptr1.next = ptr2.next   # ptr1 or ptr2 ko connect karna

                    print(key, "is deleted")

                    return

                ptr1 = ptr2
                ptr2 = ptr2.next

            print("Key not found")


if __name__ == '__main__':

    obj = Linkedlist()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("3. Add at Beginning")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Delete at Key")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()

        elif n == 2:
            obj.traverse()

        elif n == 3:
            obj.addatbefore()

        elif n == 4:
            obj.deltatbeg()

        elif n == 5:
            obj.deltatend()

        elif n == 6:
            obj.deltatkey()

        elif n == 0:
            sys.exit(0)

        else:
            print("Invalid Choice")
'''
'''
# double linked list:

import sys

class GetNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def append(self):
        data = int(input("Enter data: "))
        newNode = GetNode()
        newNode.data = data

        if self.head is None:
            self.head = newNode
        else:
            ptr = self.head

            while ptr.right != None:
                ptr = ptr.right

            ptr.right = newNode
            newNode.left = ptr

        print(data, "is added")
 
    def traverse(self):
        if self.head is None:
            print("List is not present")
        else:
            ptr = self.head

            while ptr != None:
                print(ptr.data, " -> ", end="")
                ptr = ptr.right

    def addAtBeg(self):
        data = int(input("Enter data: "))
        newNode = GetNode()
        newNode.data = data

        if self.head is None:
            self.head = newNode
        else:
            newNode.right = self.head
            self.head.left = newNode
            self.head = newNode

        print(data, "is added at beginning")

 
if __name__ == '__main__':

    obj = LinkedList()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("3. addAtBeg")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()

        if n == 2:
            obj.traverse()

        if n == 3:
            obj.addAtBeg()

        if n == 0:
            sys.exit(0)
'''
'''
import sys
class GetNode:

    def __init__(self):
        self.data = None
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self):

        data = int(input("Enter data: "))

        newNode = GetNode()
        newNode.data = data

        if self.head == None:
            self.head = newNode

        else:
            ptr = self.head

            while ptr.next != None:
                ptr = ptr.next

            ptr.next = newNode

        print(data, "is pushed")

    def pop(self):

        if self.head == None:
            print("Stack is Empty")

        elif self.head.next == None:
            print(self.head.data, "is popped")
            self.head = None

        else:
            ptr = self.head

            while ptr.next.next != None:
                ptr = ptr.next

            print(ptr.next.data, "is popped")
            ptr.next = None

    def peek(self):

        if self.head == None:
            print("Stack is Empty")

        else:
 
            print("Top Element:", self.top.data)

    def traverse(self):

        if self.head == None:
            print("Stack is Empty")

        else:
            ptr = self.head

            while ptr != None:
                print(ptr.data, " -> ", end="")
                ptr = ptr.next


if __name__ == '__main__':

    obj = Stack()

    while True:

        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.push()

        if n == 2:
            obj.pop()

        if n == 3:
            obj.peek()

        if n == 4:
            obj.traverse()

        if n == 0:
            sys.exit(0)
'''
'''
import sys


class GetNode:

    def __init__(self):
        self.data = None
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self):

        data = input("Enter data: ")

        newnode = GetNode()
        newnode.data = data

        newnode.next = self.head
        self.head = newnode

        print(data, "is pushed")

    def pop(self):

        if self.head == None:
            print("Underflow")

        else:

            ptr = self.head

            self.head = ptr.next

            print(ptr.data, "is popped")

    def peek(self):

        if self.head == None:
            print("Stack is empty")

        else:
            print("Top element is:", self.head.data)

    def traverse(self):

        if self.head == None:
            print("Stack is empty")

        else:

            ptr = self.head

            print("Stack elements:")

            while ptr != None:
                print(ptr.data)
                ptr = ptr.next


if __name__ == '__main__':

    obj = Stack()

    while True:

        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        ch = int(input("Make a choice: "))

        if ch == 1:
            obj.push()

        elif ch == 2:
            obj.pop()

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            sys.exit(0)
'''
#

price = [100, 80, 60, 75, 85]

for i in range(len(price)):

    span = 1
    j = i - 1

    while j >= 0:

        if price[j] > price[i]:
            print(1, end="")
        else:
            print(8, end="")

        j = j - 1























    







