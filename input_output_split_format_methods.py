# ****************************************output****************************************** 

print('This sentence is output to the screen')

a = 5
print('The value of a is', a)

#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')

x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))

print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'Tushar'))

x = 12.3456789
print('The value of x is %3.2f' %x)

print('The value of x is %3.4f' %x)

#********************************************input***************************************************8

num = input('Enter a number: ')
print(num)

# conversion

print(int('10'))

print(float('10'))

#int('2+3')  # error will occur

print(eval('2+3'))  # no error



# ************************************format commands****************************************************8


#  template.format(p0, p1, ..., k0=v0, k1=v1, ...)

# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

# number formatting

# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

# integer numbers with minimum width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))

# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))


# Number formatting with alignment

# integer numbers with right alignment
print("{:5d}".format(12))

# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

# integer left alignment filled with zeros
print("{:<05d}".format(12))

# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))


# string formatting with format method

# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))


# Truncating strings with format()


print("{:.3}".format("caterpillar"))

# truncating strings to 3 letters
# and padding
print("{:*<5.3}".format("caterpillar"))

# truncating strings to 3 letters,
# padding and center alignment
print("{:*^5.3}".format("caterpillar"))

#  Formatting class members using format()

class Person:
    age = 23
    name = "Adam"

print("{p.name}'s age is: {p.age}".format(p=Person()))

#  Formatting dictionary members using format()

# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{p[name]}'s age is: {p[age]}".format(p=person))

# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{name}'s age is: {age}".format(**person))

# Dynamic formatting using format()

# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))

import datetime
# datetime formatting
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

# complex number formatting
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print("Adam's age is: {:age}".format(Person()))


# __str__() and __repr__() shorthand !r and !s
print("Quotes: {0!r}, Without Quotes: {0!s}".format("cat"))

# __str__() and __repr__() implementation for class
class Person:
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

print("repr: {p!r}, str: {p!s}".format(p=Person()))




#  ****************************split method************************************ 

#   str.split(separator, maxsplit)

text = 'Python is a fun programming language'

# split the text from space
print(text.split(' '))

text= 'Love thy neighbor'

# splits at space
print(text.split())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.split(', '))

# Splits at ':'
print(grocery.split(':'))

grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 0))



