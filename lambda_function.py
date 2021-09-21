# use of lambda functions
double = lambda x: x * 2

print(double(5))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

import functools
 
 
lis = [1, 3, 5, 6, 2, ]
 
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
 
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))


import operator
 
 
lis = [1, 3, 5, 6, 2, ]
 
 
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))
 
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))
  
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["my", "name ", "is ","dahud ibrahim"]))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


 
l = ['sat', 'bat', 'cat', 'mat']
 
test = list(map(list, l))
print(test)

x ="Tushar sharma"
 
(lambda x : print(x))(x)

def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y
 
 
print(cube(5))
 
 
print(lambda_cube(5))


tables = [lambda x=x: x*10 for x in range(1, 11)]
 
for table in tables:
    print(table())

Max = lambda a, b : x if(a > b) else b
 
print(Max(1, 2))

List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
 
sortList = lambda x: (sorted(i) for i in x)
 
 
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
 
print(res)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

ages = [13, 90, 17, 59, 21, 60, 5]
 
adults = list(filter(lambda age: age>18, ages))
 
print(adults)


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(map(lambda x: x*2, li))
print(final_list)

animals = ['dog', 'cat', 'parrot', 'rabbit']
 
 
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
 
print(uppered_animals)

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)


import functools
 
 
lis = [ 1 , 3, 5, 6, 2, ]
 
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis))

my_list = ["geeks", "geeg", "keek", "practice", "aa"]
  
 
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list)) 
  
# printing the result
print(result)



















employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')