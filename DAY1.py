'''
# Armstrong Number

no = int(input("Enter no: "))
sum = 0
save = no
count = 0

# count digits
while no > 0:
    no = no // 10
    count = count + 1

no = save

# calculate sum of powers
while no > 0:
    rem = no % 10
    sum = sum + rem ** count
    no = no // 10

# check armstrong
if sum == save:
    print("no is armstrong")
else:
    print("no is not armstrong")
'''
'''
# Armstrong numbers between 1 and 10000

for i in range(1, 10001):

    no = i
    sum = 0
    save = no
    count = 0

    # count digits
    while no > 0:
        no = no // 10
        count += 1

    no = save

    # calculate power sum
    while no > 0:
        rem = no % 10
        sum = sum + rem ** count
        no = no // 10

    # check armstrong
    if sum == save:
        print("no is armstrong", i)
'''
'''
# Peterson number

no = int(input("Enter no: "))
sum = 0
save = no

while no > 0:
    rem = no % 10
    fact = 1

    while rem > 0:
        fact = fact * rem
        rem = rem - 1

    sum = sum + fact
    no = no // 10

if save == sum:
    print("no is peterson")
else:
    print("no is not peterson")
'''
'''
# there are 3 no. and find max

n1 = 10
n2 = 20
n3 = 30

max = n1

if max < n2:
    max = n2

if max < n3:
    max = n3

print(max)
'''
'''
#if-else

no = 5

if no % 2 == 0:
    print(no, "is even")
else:
    print(no, "is odd")

# if-else ladder

per = 75

if per >= 40 and per <= 60:
    print("Take admission in ABC college")

elif per >= 61 and per <= 80:
    print("Take admission in XYZ college")

elif per >= 81 and per <= 100:
    print("Take admission in PQR college")

else:
    print("Invalid percentage")
'''
'''
# remove duplicates from an unsorted array

arr = [3, 2, 3, 1, 2, 4]

ans = []

for x in arr:
    if x not in ans:
        ans.append(x)
'''
'''
# min

arr = [5, 3, 9, 2, 8]

min = arr[0]

for i in range(len(arr)):
    if min > arr[i]:
        min = arr[i]

print(min)
# max

arr = [5, 3, 9, 2, 8]

max = arr[0]

for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]

print(max)
'''
'''
# slicing

arr = [11, 22, 33, 44, 55, 66, 77, 88]

print(arr[1:5])
print(arr[4:6])
print(arr[:6])
print(arr[4:])
print(arr[:])
print(arr[::2])
print(arr[::3])
print(arr[::-2])
'''
'''
# accessing elements in the list

arr = [11, 22, 33, 44, 55, 66, 77, 88]

print(arr[3])
print(arr[-1])
# traversing of the list

arr = [11, 22, 33, 44, 55, 66, 77, 88]
print(arr)

for i in range(len(arr)):
    print(arr[i])

arr = [11, 22, 33, 44, 55, 66, 77, 88]
print(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")

print()

for x in arr:
    print(x, end=" ")
'''
'''
# for loop

for i in range(10):
    print(i)
# updation

for i in range(1, 11, 3):
    print(i)
# print range
for i in range(10, 0, -2):
    print(i)
# array
arr = [1, 2, 3, 4, 5]

for i in range(len(arr)):
    print(arr[i])

for x in arr:
    print(x)
# while loop
i = 1
j = 10

while i < j:

    if i == 3:
        i = i + 1
        j = j - 1
        continue

    print(i, "\t", j)

    i = i + 1
    j = j - 1
# how to create a list in ds(python)

ls = []
print(type(ls))

ls = list()
print(type(ls))

ls = [1, 2, 3, 34, 77, 88]
print(type(ls))
'''
'''
n = int(input("Enter no: "))

n1 = n % 10
n = n // 10

n2 = n % 10
n = n // 10

n3 = n % 10

rev = n1 * 100 + n2 * 10 + n3
print(rev)
'''
'''
n = int(input("Enter 9 digit number: "))

last = n % 10
first = n // 100000000

sum = first + last

print("Sum =", sum)
'''
'''
n = int(input("Enter number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse =", rev)
'''
'''
n = int(input("Enter number: "))

count = 0

while n > 0:
    n = n // 10
    count += 1

print("Total digits =", count)
'''
'''
n = int(input("Enter number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)
'''
'''
n = int(input("Enter 3 digit number: "))

d1 = n % 10
n = n // 10

d2 = n % 10
n = n // 10

d3 = n % 10

sum = d1 + d2 + d3

print("Sum =", sum)
'''
'''
n = int(input("Enter 5 digit number: "))

d1 = n % 10
n = n // 10

d2 = n % 10
n = n // 10

d3 = n % 10
n = n // 10

d4 = n % 10
n = n // 10

d5 = n % 10

sum = d1 + d2 + d3 + d4 + d5

print("Sum =", sum)
'''
'''
n = int(input("Enter 2 digit number: "))

d1 = n % 10
d2 = n // 10

sum = d1 + d2

print("Sum =", sum)
'''
'''
n = int(input("Enter number: "))

last = n % 10

print("Last digit =", last)
'''
cp = int(input("Enter cost price: "))
s = input("Student or not (yes/no): ")

if s == "yes":
    print("Bill =", cp - cp*10/100)
else:
    print("Bill =", cp - cp*5/100)


