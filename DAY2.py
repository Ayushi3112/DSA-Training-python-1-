'''

# array que1
arr=[[1,2,3],22,[4,5]]
print(arr)
for x in range(len(arr)):
   print(arr[x])
'''
'''
# array que2
arr=[[1,2,3],[4,5,6],[7,8,9]]
print(arr)
for x in range(len(arr)):
    print(arr[x])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()
'''
'''
# que3 set
s=set()
print(s)
print(type(s))

s={1,2,3,4,5,3,2,4,3,2,4,4}
print(s)
'''
'''
#accept values from user & print it
n=int(input("Enter size: "))
print(" Enter list element: ")
arr=[]
for i in range(n):
    ele=int(input("Enter element: "))
    arr.append(ele)

for i in range(len(arr)):
    print(arr[i])
'''
'''
# accept values from user and find sum of list

n = int(input("Enter size: "))

print("Enter list elements:")

arr = []

for i in range(n):
    ele = int(input("Enter element: "))
    arr.append(ele)

sum = 0

for i in range(len(arr)):
    print(arr[i])
    sum = sum + arr[i]

print("Sum =", sum)
'''
'''
# sum of even and odd numbers

n = int(input("Enter size: "))

print("Enter list elements:")

arr = []

even = 0
odd = 0
e1 = 0
o1 = 0

for i in range(n):
    ele = int(input("Enter element: "))
    arr.append(ele)

for i in range(len(arr)):

    if arr[i] % 2 == 0:
        even = even + arr[i]
        e1 = e1 + 1

    else:
        odd = odd + arr[i]
        o1 = o1 + 1

print("Sum of even Numbers =", even)
print("Sum of odd Numbers =", odd)
'''
'''
# Tech number

no = int(input("Enter no: "))

n1 = no % 100
n2 = no // 100

sum = n1 + n2
sq = sum * sum

if sq == no:
    print("no is tech number")
else:
    print("no is not tech number")
'''
'''
# Tech number using digit count

no = int(input("Enter no: "))

save = no
count = 0

while no > 0:
    no = no // 10
    count = count + 1

no = save
if count % 2 == 0:

    mid = count // 2

    n1 = no % (10 ** mid)
    n2 = no // (10 ** mid)

    sum = n1 + n2
    sq = sum * sum

    if sq == no:
        print("no is tech number")
    else:
        print("no is not tech number")

else:
    print("no is not tech number")
'''
'''
# pattern programming
for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()
# pattern que1
n=1
for i in range(1,5):
    for j in range(1,5):
        print(n,end=" \t")
        n=n+1
    print()
'''
'''
# pattern que2
n=65
for i in range(1,5):
    for j in range(1,5):
        print(chr(n),end=" \t")
        n=n+1
    print()
'''
'''
# que3
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="")
    print()
'''
'''
#que4
sp=0
for i in range(4,0,-1):
    for x in range(sp):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
    sp=sp+1
'''
'''
#que5
s="ayushi"
print(s)
s='ayushi'
print(s)
s="""" DSA programming training"""
print(s)
'''
'''
# reverse the string
s="ayushi"
print(s[::-1])
'''
'''
s="Learning Python is very easy from Ashish Sir"
print(s.find("Python"))
print(s.find("Java"))
print(s.find("r"))
print(s.rfind("r"))
'''
'''
s="abcabcabcabcadda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a',3,10))
'''
'''
s="Learning Python is very difficult from Ashish Sir"
s1=s.replace("difficult","easy")
print(s1)
'''
'''
s="Learning Python is very difficult from Ashish Sir"
ls=s.split()
print(ls)
print(len(ls))
'''
'''
s="22-02-2022"
ls=s.split("-")
print(ls)

s="www.ayushi.com"
ls=s.split(".")
print(ls)
'''
'''
# joining of the string
l=['Nagpur','Pune','Mumbai','Delhi']
s=' '.join(l)
print(s)


s=input("Enter string:")
print(':'.join(reversed(s)))
'''
'''
s=input("Learning Python is easy from Ashish Sir")
ls=s.split()
print(ls)
print(s[::-1])
print(ls)
s=" ".join(ls)
print(s)
'''
'''
s=input("Learning Python is easy from Ashish Sir")
ls=s.split()
print(ls)
ans=""
for x in range(len(ls)):
   ans=ans+ls[x][::-1]+" "
print(ans)
'''
'''
s=input("Learning python is easy from ashish sir")
ans=""
for x in s:
   if x not in ans:
      ans=ans+x
   print(ans)
'''
'''
no = input("Enter numbers: ")

if no.isdigit():

    if len(no) == 10:

        if no.startswith('6') or no.startswith('7'):
            print("valid indian mobile number")

        else:
            print("invalid indian mobile number")

    else:
        print("invalid indian mobile number")

else:
    print("please enter number in digit format only")
'''
'''
#dictionary:
d={}
d[100]="Ashish"
d[200]="Naman"
d[300]="Tanishq"
print(d)
'''
'''
rec={}
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter name: ")
    per=float(input("Enter perc: "))
    rec[name]=per

print(rec)
for x in rec:
    print(x,"/t",rec[x])
'''























