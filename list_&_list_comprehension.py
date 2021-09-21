my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[0])  # p

print(my_list[2])  # o

print(my_list[4]) # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])
 
print(my_list[-1])

print(my_list[-5])

my_list = ['p','r','o','f','e','s','s','i','o','n','a','l']

# includes element at index 2, 3, 4
# excludes element at index 5
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

print(odd) 
# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)
# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])

print(["re"] * 3)
# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)

print(odd)

odd[2:2] = [5, 7]

print(odd)
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete entire list
del my_list
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

 
print(my_list)

 
print(my_list.pop(1))

 
print(my_list)

 
print(my_list.pop())

 
print(my_list)

my_list.clear()

 
print(my_list)
#Finally, we can also delete items in a list by assigning an empty list to a slice of elements.
my_list = ['p','r','o','b','l','e','m']
my_list[2:3] = []
print(my_list)
 
my_list = [3, 8, 1, 6, 0, 8, 4]

 
print(my_list.index(8))

 
print(my_list.count(8))

my_list.sort()

 
print(my_list)

my_list.reverse()
 
print(my_list)

''' list comprehension examples'''

pow2 = [2 ** x for x in range(10)]
print(pow2)

print([x+y for x in ['Python ','C '] for y in ['Language','Programming']])

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

 
print('p' in my_list)
 
print('a' in my_list)
 
print('c' not in my_list)

for fruit in ['apple','banana','mango']:
    print("I like",fruit)


#  list methods *************
 
animals = ['cat', 'dog', 'rabbit']

 
wild_animals = ['tiger', 'fox']

 
animals.append(wild_animals)

print('Updated animals list: ', animals)  

currencies = ['Dollar', 'Euro', 'Pound']

# append 'Yen' to the list
currencies.append('Yen')

print(currencies)

vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')

print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')


print('The index of i:', index)

vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'p' is vowels
index = vowels.index('p')

print('The index of p:', index)

# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

 
index = alphabets.index('e')    

print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)    

print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)   

print('The index of i:', index)

# extend method

prime_numbers = [2, 3, 5]

 
numbers = [1, 4]

# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)


print('List after extend():', numbers)

# Output: List after extend(): [1, 4, 2, 3, 5]

languages = ['French']

# languages tuple
languages_tuple = ('Spanish', 'Portuguese')

# languages set
languages_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
languages.extend(languages_tuple)


print('New Language List:', languages)

# appending language_set elements to language
languages.extend(languages_set)


print('Newer Languages List:', languages)

a = [1, 2]
b = [3, 4]

a += b     

print('a =', a)

a = [1, 2]
b = [3, 4]

a[len(a):] = b

print('a =', a)

# difference b/w extend and append

a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

 
a1.extend(b) 
print(a1)

a2.append(b)
print(a2)


#insert(index,element to be inserted) method

vowel = ['a', 'e', 'i', 'u']
vowel.insert(3, 'o')


print('List:', vowel)

 
prime_numbers = [2, 3, 5, 7]

# insert 11 at index 4
prime_numbers.insert(4, 11)


print('List:', prime_numbers)

mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list.insert(1, number_tuple)


print('Updated List:', mixed_list)


# remove method 

prime_numbers = [2, 3, 5, 7, 9, 11]
 #  removes first occurance
prime_numbers.remove(9)
print('Updated List: ', prime_numbers)

animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

animals.remove('dog')
print('Updated animals list: ', animals)


#   count method

numbers = [2, 3, 5, 2, 11, 2, 7]

# check the count of 2
count = numbers.count(2)


print('Count of 2:', count)
 

random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))


 
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])


print("The count of [3, 4] is:", count)

#  pop() method  pop() method removes the item at the given index from the list and returns the removed item.

prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)

#  the default index -1 is passed as an argument (index of the last item).

languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)

print('Return Value:', return_value)

print('Updated List:', languages)


print('When index is not passed:') 
print('Return Value:', languages.pop())

print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:') 
print('Return Value:', languages.pop(-1))

print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:') 
print('Return Value:', languages.pop(-3))

print('Updated List:', languages)


# reverse method  


prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)

# reversing using slicing operator

systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list	
# Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]


# updated list
print('Updated List:', reversed_list)

# using reversed method
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)


# sort method  

prime_numbers = [11, 3, 7, 5, 2]

# sort the list
prime_numbers.sort()
print(prime_numbers)


# Note: The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, while sorted() doesn't change the list and returns the sorted list.

vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

print('Sorted list (in Descending):', vowels)

# sorting according to different parameter using key parameter

def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

print('Sorted list:', random)

employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')


#  copy method

my_list = ['cat', 0, 6.7]

 
new_list = my_list.copy()


print('Copied List:', new_list)

'''We can also use the = operator to copy a list. For example,

old_list = [1, 2, 3]
new_list = old_list
Howerver, there is one problem with copying lists in this way.
If you modify new_list, old_list is also modified. It is because the new list is referencing or pointing to the same old_list object.'''


old_list = [1, 2, 3]

# copy list using =
new_list = old_list


# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)


# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]


# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)



# clear method in python  


#  using clear method 
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()


print('List:', list)

# using slicing operator  


list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]


print('List:', list)