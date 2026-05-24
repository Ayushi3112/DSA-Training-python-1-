'''
#merge sort with sorted List
class MergeSort:
    def mergeSort(self, arr1, arr2):
        arr3=[]
        i=0
        j=0
        k=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr3.append(arr1[j])
                i+=1
                k+=1
            else:
                arr3.append(arr2[j])
                j+=1
                k+=1

        return arr3

if __name__ == '__main__':
    obj = MergeSort()
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]

    ans = obj.mergeSort(arr1, arr2)
    print(ans)
'''
'''
#merge sort with sorted List
class MergeSort:
    def mergeSort(self, arr1, arr2):
        arr3=[]
        i=0
        j=0
        k=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr3.append(arr1[j])
                i+=1
                k+=1
            else:
                arr3.append(arr2[j])
                j+=1
                k+=1
        while len(arr1)>i:
            arr3.append(arr1[i])
            i+=1
            k+=1
        while len(arr2)>j:
            arr3.append(arr2[j])
            j+=1
            k+=1


        return arr3

if __name__ == '__main__':
    obj = MergeSort()
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]

    ans = obj.mergeSort(arr1, arr2)
    print(ans)
'''
'''
# linked list
  
import sys

class GetNode:
    def __int__(self):
        self.data=None
        self.next=None
class Linkedlist:
    def __int__(self):
        self.head=None
    def append(self):
        pass

    def traverse(self):
        pass

if __name__ == '__main__':
    obj = Linkedlist()
    while True:
       print("1. Append")
       print("2. Traverse")
       print("0. Exit")
       n=int(input("Select any choice: "))
       if n==1:
          obj.append()
       elif n==2:
          obj.traverse()
       elif n==0:
           sys.exit(0)
'''
'''
# linked list

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

            print("None")


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

        else:
            print("Invalid Choice")
'''
'''
# linked list
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
                def addinbegin(self):
                    data = int(input("Enter data: "))
                    newNode = GetNode()
                    newNode.data = data
                    ptr = self.head
                    if self.head == None:
                       self.head = newNode
                    else:
                        newNode.next = ptr
                        self.head = newNode
                    print(data, "is added in beginning")


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
# linked list
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
                def addbetwn(self):
                    data = int(input("Enter data: "))
                    Key=int(input("Enter data after inserted: "))
                    newNode = GetNode()
                    newNode.data = data

                    if self.head == None:
                       self.head = newNode
                    else:
                        ptr=self.head
                        while ptr.next!=None:
                            if key==ptr.data:
                                break;
                            else:
                                ptr=ptr.next
                            if  ptr.next==None:
                                print("key not found")
                            else:
                                ptr1=ptr.next
                                ptr.next=newNode
                                newNode.next=ptr1

                                print(data," is added")





if __name__ == '__main__':

    obj = Linkedlist()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("3. addbetwn")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()
        if n == 2:
            obj.traverse()
        if n == 3:
            obj.addbetwn()

        if n == 0:
            sys.exit(0)
'''




