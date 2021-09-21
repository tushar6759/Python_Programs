# string 
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

#Accessing string characters in Python
str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

#If we try to access an index out of the range or use numbers other than an integer, we will get errors
#my_string[15]  
#IndexError: string index out of range

# index must be an integer
#my_string[1.5] 
#TypeError: string indices must be integers

#Strings are immutable. This means that elements of a string cannot be changed once they have been assigned. We can simply reassign different strings to the same name.

my_string = 'programiz'
#my_string[5] = 'a' #error
...
#TypeError: 'str' object does not support item assignment
my_string = 'Python'
print(my_string)

#We cannot delete or remove characters from a string. But deleting the string entirely is possible using the del keyword.

#del my_string[1]    error
del my_string
#print(my_string)
#NameError: name 'my_string' is not defined

# Python String Operations
str1 = 'Hello'
str2 ='World!'

 
print('str1 + str2 = ', str1 + str2)

print('str1 * 3 =', str1 * 3)

# two string literals together
print('Hello ''World!')
 # using parentheses
s = ('Hello ''World')
print(s)


# Iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

#String Membership Test

print('a' in 'program')
print('at' not in 'battle')

#Built-in functions  

str = 'cold'

list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

#Python String Formatting

# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")

#Sometimes we may wish to ignore the escape sequences inside a string. To do this we can place r or R in front of the string. 

print("This is \x61 \ngood example")
print(r"This is \x61 \ngood example")

 
#Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)


# formatting integers

print("Binary representation of {0} is {0:b}".format(12))

# formatting floats

print("Exponent representation: {0:e}".format(1566.345))
'Exponent representation: 1.566345e+03'

# round off
print("One third is: {0:.3f}".format(1/3))

#string alignment

print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))

# c style formatting

x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)

print("PrOgRaM".lower())
print("PrOgRaMiZ".upper())

print("This will split all words into a list".split())
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
# finding index of substring

print('Happy New Year'.find('ew'))

print('Happy New Year'.replace('Happy','Brilliant'))
