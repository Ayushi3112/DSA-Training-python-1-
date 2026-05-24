'''
s = "yce"
t = "ycsce"

count = 0

if len(s) < len(t):
    output = len(t) - len(s)

elif len(t) < len(s):
    output = len(s) - len(t)

else:
    for i in range(len(s)):

        if s[i] != t[i]:
            count = count + 1

    output = count

print(output)
'''
'''
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


if __name__ == '__main__':

    obj = LinkedList()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()

        if n == 2:
            obj.traverse()

        if n == 0:
            sys.exit(0)
'''
'''
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
    def addAtEnd(self):
        data = int(input("Enter data: "))
        newNode = GetNode()
        newNode.data = data
        # if list is empty
        if self.head is None:
            self.head = newNode
        else:
            ptr = self.head
        # move to last node
        while ptr.right is not None:
             ptr = ptr.right
        # add new node at end
        ptr.right = newNode
        newNode.left = ptr
        print(data, "is added at end")

if __name__ == '__main__':

    obj = LinkedList()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("3. addAtBeg")
        print("4. addAtEnd")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()

        if n == 2:
            obj.traverse()

        if n == 3:
            obj.addAtBeg()

        if n == 4:
            obj.addAtEnd()
        if n == 0:
            sys.exit(0)
'''
'''
# implement a stack using singly linked list
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
'''




