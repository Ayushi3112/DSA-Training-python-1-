'''
# factorial of no with recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

if __name__ == '__main__':
    n=5
    res=fact(n)
    print(res)
'''
'''
# multiply  2 no with recursion
def multiply(x, y):

    if y == 0:
        return 0

    return x + multiply(x, y - 1)


def main():

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Multiplication =", multiply(x, y))


if __name__ == "__main__":
    main()
'''
'''
# find power using recursion

def power(x, y):

    if y == 1:
        return x

    elif x == 1:
        return 1

    elif x == 0:
        return 0

    elif y == 0:
        return 1

    return x * power(x, y - 1)

if __name__ == "__main__":
    x=2
    y=3
    res=power(x,y)
    print(res)
'''
'''
# find sum of n numbers using recursion

def sumN(n):

    if n == 1:
        return 1

    elif n == 0:
        return 0

    else:
        return n + sumN(n - 1)


if __name__ == "__main__":

    n = 10
    res = sumN(n)

    print(res)
'''
'''
# find sum of n numbers using recursion

def fibo(n):

    if n == 0:
        return 0;

    elif n == 1:
        return 1;

    else:
        return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    n = 10
for x in range(n):
    print(fibo(x),end=" ")
'''
'''
import sys
class Graph:
    def __int__(self):
        self.nodes=[]
        self.graph=[]
        self.nodeCount=0
        
    def addNode(self,v):
        
        if v in self.nodes:
            print(v,"is already present")
            
        else:
            self.nodeCount+=1
            self.nodes.append(v)
            
            for x in self.graph:
                x.append(0)
                
            temp=[]
            for x in range(self.nodeCount):
              temp.append(0)  
            self.graph.append(temp)
            
            print(v,"is added")
        
    def addedge_undirected_unweighted(self,v1,v2):
        if v1 not in self.nodes:
            print(v1,"not present")
            return
        if v2 not in self.nodes:
            print(v2,"not present")
            return
        index1=self.node.index(v1)
        index2=self.node.index(v2)
        
        self.graph[index1][index2]=1
        self.graph[index2][index1]=1
        
        print("Edge added successfully")
        
    def addedge_undirected_weighted(self,v1,v2,weighted):
        pass
    def addNode_Directed_weighted(self):
        pass
    def printGraph(self):
        print(*self.node)
        for i in range(self.nodeCount):
            for j in range(self.nodeCount):
                print(self.graph[i][j],end=" ")
                print()
                def deletenode(self):
                    pass
                obj=Graph()
                while True:
                    print("\n1.(Insertion) add node using adjacency matrix representation")
                    print("2.(Insertion) add edge using adjacency matrix representation")
                    print("3. (Insertion) add a edge")
                    n=int(input("Enter any choice:"))
                    if n==1:
                        v=input("Enter vertex:")
                        obj.addnode(v)
                    elif n==2:
                        v1=input("Enter vertex1:")
                        v2=input("Enter vertex2:")
                        obj.addedge_undirected_unweighted(v1,v2)
           
                    elif n==3:
           
                         v1=input("Enter vertex1:")
                         v2=input("Enter vertex2:")
                         obj.addedge_undirected_weighted(v1,v2)
           
                    elif n==4:
                         obj.addnode_Directed_weighted()
            
                    elif n==5:
                         obj.printGraph()
            
                    elif n==6:
                         obj.deletenode()
            
                    elif n==0:
                          sys.exit()
'''
'''
# inheritance


# single inheritance
class A:
    def showA(self):
        print("I am in class A")
class B(A):
    def showB(self):
        print("I am in class B")
if __name__ == '__main__':
    obj=B()
    obj.showA()
    obj.showB()
'''
'''
# multilevel inheritance:
class A:
    def showA(self):
        print("I am in class A")
class B(A):
    def showB(self):
        print("I am in class B")
class C(B):
    def showC(self):
        print("I am in class C")
if __name__ == '__main__':
    obj=C()
    obj.showA()
    obj.showB()
    obj.showC()
'''
'''
# multiple inheritance

class A:
    def showA(self):
        print("I am in class A")

class B:
    def showB(self):
        print("I am in class B")

class C(A, B):
    def showC(self):
        print("I am in class C")

if __name__ == '__main__':
    obj = C()
    obj.showA()
    obj.showB()
    obj.showC()
'''
'''
# hierarchical inheritance

class A:
    def showA(self):
        print("I am in class A")

class B(A):
    def showB(self):
        print("I am in class B")

class C(A):
    def showC(self):
        print("I am in class C")

if __name__ == '__main__':
    obj1 = B()
    obj1.showA()
    obj1.showB()

    obj2 = C()
    obj2.showA()
    obj2.showC()
'''
'''
# hybrid inheritance

class A:
    def showA(self):
        print("I am in class A")

class B(A):
    def showB(self):
        print("I am in class B")

class C(A):
    def showC(self):
        print("I am in class C")

class D(B, C):
    def showD(self):
        print("I am in class D")

if __name__ == '__main__':
    obj = D()

    obj.showA()
    obj.showB()
    obj.showC()
    obj.showD()
'''
'''
# polymorphism
def add(a):
    print(a)
    
def add(a,b):
    print(a+b)
    
def add(a,b,c):
    print(a+b+c)

# add(11)
# add(22,33)
add(11,22,33)
'''
# polymorphism overriding

class Parent:
    def __init__(self):
        print("cash,gold")
        
    def bike(self):
        print("splender+")
class Child(Parent):
    def bike(self):
        print("HB")
        
obj=Child()
obj.bike()

# polymorphism overriding

class Parent:
    def __init__(self):
        self.speed=100
        print("cash,gold")
        
    def bike(self):
        print("splender+",self.speed)
        
class Child(Parent):
    def __init__(self):
        self.speed=150
    def bike(self):
        print("HB",self.speed)
        
obj=Child()
obj.bike()









            













