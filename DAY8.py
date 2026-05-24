'''
# implement Binary Search Tree
import sys

class BST:

    def __init__(self, key=None):
        self.leftchild = None
        self.data = key
        self.rightchild = None

    # insert node
    def insert(self):

        key = int(input("Enter value: "))

        # first node
        if self.data is None:
            self.data = key
            return

        ptr = self

        while True:

            # insert in left side
            if key < ptr.data:

                if ptr.leftchild is None:
                    ptr.leftchild = BST(key)
                    break
                else:
                    ptr = ptr.leftchild

            # insert in right side
            else:

                if ptr.rightchild is None:
                    ptr.rightchild = BST(key)
                    break
                else:
                    ptr = ptr.rightchild

    # inorder traversal
    def inorder(self):

        if self.leftchild:
            self.leftchild.inorder()

        if self.data is not None:
            print(self.data, end=" ")

        if self.rightchild:
            self.rightchild.inorder()

    # preorder traversal
    def preorder(self):

        if self.data is not None:
            print(self.data, end=" ")

        if self.leftchild:
            self.leftchild.preorder()

        if self.rightchild:
            self.rightchild.preorder()

    # postorder traversal
    def postorder(self):

        if self.leftchild:
            self.leftchild.postorder()

        if self.rightchild:
            self.rightchild.postorder()

        if self.data is not None:
            print(self.data, end=" ")


if __name__ == '__main__':

    root = BST()

    while True:

        print("\n1. Insert")
        print("2. Postorder")
        print("3. Preorder")
        print("4. Inorder")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            root.insert()

        elif n == 2:
            print("Postorder Traversal:")
            root.postorder()

        elif n == 3:
            print("Preorder Traversal:")
            root.preorder()

        elif n == 4:
            print("Inorder Traversal:")
            root.inorder()

        elif n == 0:
            sys.exit()

        else:
            print("Invalid choice")
'''
'''
#( implement Binary Search)
import sys
class BST:

    def __init__(self, key=None):
        self.leftchild = None
        self.data = key
        self.rightchild = None

    def insert(self, key):

        if self.data is None:
            self.data = key
            return

        elif self.data == key:
            return

        else:

            if key < self.data:

                if self.leftchild:
                    self.leftchild.insert(key)

                else:
                    self.leftchild = BST(key)

            elif key > self.data:

                if self.rightchild:
                    self.rightchild.insert(key)

                else:
                    self.rightchild = BST(key)

    def preorder(self):

        print(self.data, end=" -> ")

        if self.leftchild:
            self.leftchild.preorder()

        if self.rightchild:
            self.rightchild.preorder()

    def postorder(self):

        if self.leftchild:
            self.leftchild.postorder()

        if self.rightchild:
            self.rightchild.postorder()

        print(self.data, end=" -> ")

    def inorder(self):

        if self.leftchild:
            self.leftchild.inorder()

        print(self.data, end=" -> ")

        if self.rightchild:
            self.rightchild.inorder()


if __name__ == '__main__':

    root = BST()

    while True:

        print("\n1. insert")
        print("2. postorder")
        print("3. preorder")
        print("4. inorder")
        print("0. Exit")

        n = int(input("\nSelect any choice: "))

        if n == 1:

            arr = [36, 26, 46, 21, 31, 11, 24, 41, 56, 51, 66]

            for i in range(len(arr)):
                root.insert(arr[i])

            print("Nodes inserted")

        elif n == 2:
            root.postorder()
            print()

        elif n == 3:
            root.preorder()
            print()

        elif n == 4:
            root.inorder()
            print()

        elif n == 0:
            sys.exit()

        else:
            print("Invalid choice")
'''
'''
# search
import sys
class BST:

    def __init__(self, key=None):
        self.leftchild = None
        self.data = key
        self.rightchild = None

    def insert(self, key):

        if self.data is None:
            self.data = key
            return

        elif self.data == key:
            return

        else:

            if key < self.data:

                if self.leftchild:
                    self.leftchild.insert(key)

                else:
                    self.leftchild = BST(key)

            elif key > self.data:

                if self.rightchild:
                    self.rightchild.insert(key)

                else:
                    self.rightchild = BST(key)

    def search(self, key):

        if self.data == key:
            return "Node Found"

        elif key < self.data:

            if self.leftchild:
                return self.leftchild.search(key)

            else:
                return "Node Not Found"

        else:

            if self.rightchild:
                return self.rightchild.search(key)

            else:
                return "Node Not Found"

    def preorder(self):

        print(self.data, end=" -> ")

        if self.leftchild:
            self.leftchild.preorder()

        if self.rightchild:
            self.rightchild.preorder()

    def postorder(self):

        if self.leftchild:
            self.leftchild.postorder()

        if self.rightchild:
            self.rightchild.postorder()

        print(self.data, end=" -> ")

    def inorder(self):

        if self.leftchild:
            self.leftchild.inorder()

        print(self.data, end=" -> ")

        if self.rightchild:
            self.rightchild.inorder()


if __name__ == '__main__':

    root = BST()

    while True:

        print("\n1. insert")
        print("2. postorder")
        print("3. preorder")
        print("4. inorder")
        print("5. search")
        print("0. Exit")

        n = int(input("\nSelect any choice: "))

        if n == 1:

            arr = [36, 26, 46, 21, 31, 11, 24, 41, 56, 51, 66]

            for i in range(len(arr)):
                root.insert(arr[i])

            print("Nodes inserted")

        elif n == 2:
            root.postorder()
            print()

        elif n == 3:
            root.preorder()
            print()

        elif n == 4:
            root.inorder()
            print()

        elif n == 5:

            key = int(input("Enter value to search: "))
            print(root.search(key))

        elif n == 0:
            sys.exit()

        else:
            print("Invalid choice")
'''






