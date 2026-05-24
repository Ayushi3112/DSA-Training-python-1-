'''
#ADD
def add():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    res=a+b
    print("Addition is ",res)
add()
'''
'''
# function with return and parameterized value
def add(a,b):
  res=a+b
  return res

a=int(input("Enter a: "))
b=int(input("Enter b: "))

r=add(a,b)

print("Addition is ",r)
'''
'''
# return multiple results
def add(a,b):
  res1=a+b
  res2=a-b
  res3=a*b
  return res1,res2,res3

a=int(input("Enter a: "))
b=int(input("Enter b: "))

r1,r2,r3=add(a,b)

print("Addition is ",r1)
print("Subtraction is ",r2)
print("Multiply is ",r3)
'''
'''
# Linear search
def linear_search(n,arr,target):
    flag=False
    
    for i in range(n):
        if target!=arr[i]:
            pass
        else:
            flag=True
            loc=i

    if flag==True:
        print("Search is successful and present at ",loc)
    else:
        print("Search is unsuccessful")

n=int(input("Enter size: "))

arr=[]

for i in range(n):
    arr.append(int(input()))

target=int(input("Enter no which is to be search: "))

linear_search(n,arr,target)
'''
'''
# Binary search
def binary_search(n,arr,target):
    flag=False
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            flag=True
            loc=i
            low=mid
            break;
        elif target<arr[mid]:
            high=mid-1
        elif target>arr[mid]:
            low=mid+1
    if flag==True:
        print("Search is successful and present at ",loc)
    else:
        print("Search is unsuccessful")

n=int(input("Enter size: "))
arr=[]
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter no which is to be search: "))
binary_search(n,arr,target)
'''
'''
# Next Larger Element

n = int(input("Enter size: "))

arr = []

print("Enter elements:")

for i in range(n):
    arr.append(int(input()))

ans = []

for i in range(n):

    larger = -1

    for j in range(i + 1, n):

        if arr[j] > arr[i]:
            larger = arr[j]
            break

    ans.append(larger)

print("Next larger elements are:")

for i in ans:
    print(i, end=" ")
'''

