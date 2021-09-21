# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#A tuple can also be created without using parentheses. This is known as tuple packing.
my_tuple = 3, 4.6, "dog"
print(my_tuple)
type(my_tuple)

# tuple unpacking  
a, b, c = my_tuple

print(a)      
print(b)     
print(c)      

my_tuple = ("hello")
print(type(my_tuple)) 

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  

#indexing

# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])    
print(my_tuple[5])  

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])      
print(n_tuple[1][1])       

# Negative indexing  
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

 
print(my_tuple[-1])

 
print(my_tuple[-6])

#slicing

# Accessing tuple elements using slicing
my_tuple = ('p','r','o','g','r','a','m','i','z')

 
print(my_tuple[1:4])

 
print(my_tuple[:-7])

 
print(my_tuple[7:])

# elements beginning to end
print(my_tuple[:])

#Changing a Tuple

# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])


# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9    
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(my_tuple)

# Concatenation
print((1, 2, 3) + (4, 5, 6))

# Repeat
print(("Repeat",) * 3)

# Deleting tuples
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
print(my_tuple)

#Tuple Methods

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  
print(my_tuple.index('l'))   

# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple)
print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)

# Using a for loop to iterate through a tuple
for name in ('Tushar', 'Harsh'):
    print("Hello", name)

# advantages of tuple over list

''' 
We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.'''