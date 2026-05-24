
# Enter number of semesters
'''
n = int(input("Enter no of semesters: "))

subjects = []

# Input number of subjects in each semester
for i in range(n):
    s = int(input(f"Enter no of subjects in {i+1} semester: "))
    subjects.append(s)

# Input marks and find maximum marks
for i in range(n):
    print(f"Marks obtained in semester {i+1}:")
    
    max_mark = -1

    for j in range(subjects[i]):
        mark = int(input())

        if mark < 0 or mark > 100:
            print("You have entered invalid mark")
            exit()

        if mark > max_mark:
            max_mark = mark

    print(f"Maximum mark in {i+1} semester: {max_mark}")
'''

# Python Implementation
'''
class HashTable:
    def __init__(self, size):   
        self.size = size       
        
        self.table=[]
        for i in range(size):
            self.table.append([])
            
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key=35):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        for x in range(10):
            print(self.table[x])

h = HashTable(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()
'''

# Linear Probing:
'''
class Linearprobing:
    
    def __init__(self, size):   
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = key

    def display(self):
        print(self.table)


h = Linearprobing(10)

h.insert(15)
h.insert(25)
h.insert(35)

h.display()
'''

# Build Hash Table Manually
'''
class MyHashFunction:

    def __init__(self, size):  
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key , value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return "Not Found"

    def delete(self, key):
        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

    def display(self):
        print(self.table)


h = MyHashFunction(10)

h.insert(1, "Naman")
h.insert(11, "Tanishq")
print(h.search(11))

h.display()

h.delete(11)

h.display()

        


'''
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            current_num = nums[i]
            complement = target - current_num

            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[current_num] = i
            return [i, j]
'''

#regular expression
'''
import re
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("abaababaab")
#print(matcher)
for match in matcher:
    count+=1
    print(match.start(),'...',match.end(),'...',match.group())
    print("total no of group occurrences: ",count)
'''
# pass pattern to finditer()
'''
import re
count=0
#pattern=re.compile("ab")
#matcher=pattern.finditer("abaababaab")
matcher=re.finditer("ab","abaababaab")
for match in matcher:
    count+=1
    print(match.start(),'...',match.end(),'...',match.group())
    print("total no of group occurrences: ",count)
'''
'''
import re
#x="[abc]"
#x="[^abc]"
x="[a-z]"
#x="[0-9]"
#x="[a-zA-Z0-9]"
#x="[^a-zA-Z0-9]"
matcher=re.finditer(x,"a7bD2@k2$D8z")
for match in matcher:
    print(match.start(),'...',match.end(),'...',match.group())
'''
'''
import re
#x="\\s"
#x="\\S"
#x="\\d"
x="\\D"
#x="\\w"
#x="\\W"
#x="."
matcher=re.finditer(x,"a7bD2@k2$D8z")
for match in matcher:
    print(match.start(),'...',match.end(),'...',match.group())
'''
#Quantifier
'''
import re
#x= "a"
#x= "a+"
#x= "a+"
#x= "a*"
#x= "a?"
#x= "a{3}"
x= "a{2,3}"
matcher=re.finditer(x,"abaababaabaaabaaaa")
for match in matcher:
    print(match.start(),'...',match.end(),'...',match.group())
'''
# match function
'''
import re
str=input("Enter any string : ")
m=re.match(str,"abc@xyz_pqr*")
if m!=None:
    print("Yes matching is available at beg")
    print('start index: ',match.start(),'.end index:'.m.end())
else:
    print("matching is not available at beg")
'''
# full match
'''
import re
str=input("Enter any string : ")
m=re.match("abc@xyz_pqr\\*",str)
if m!=None:
    print("Yes matching is available at beg")
    print('start index: ',m.start(),'.end index:',m.end())
else:
    print("matching is not available at beg")
'''
# findall
'''
import re
list=re.findall("[0-9]","ab4#f7p@5qrs9")
print(list)
for x in list:
    print(x)
'''
# replacement
'''
import re
str=re.sub("[a-z]","$","ab4#f7p@5qrs9")
print(str)
print(type(str))
'''

# 10 digit no
'''
import re
number=input("Enter mobile number")
match=re.fullmatch("[6-9]\\d{9}",number)
if match!=None:
    print(number," is valid mobile number")
else:
    print(number," is  not valid mobile number")
'''

    
    


    






