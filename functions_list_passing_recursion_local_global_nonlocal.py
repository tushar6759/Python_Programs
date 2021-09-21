#*****************  functions*******************
# defining document string  and accessing it using __doc__attribute 

def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")
print(greet.__doc__)

greet('Tushar sharma')

#  Note: In python, the function definition should always be present before the function call.

#  if  return statement itself is not present inside a function, then the function will return the None object.

# example

print(greet("May"))

def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))

#  Parameters and variables defined inside a function are not visible from outside the function. Hence, they have a local scope.

#  The lifetime of a variable is the period throughout which the variable exits in the memory. The lifetime of variables inside a function is as long as the function executes.

# They are destroyed once we return from the function. Hence, a function does not remember the value of a variable from its previous calls.

def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)  # x inside the function is different (local to the function) from the one outside.

greet(name = "Tushar",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Tushar") 

greet("Tushar", msg = "How do you do?")    

# *********************passing tuple as argument in function******************************

def greeting(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greeting("Monica", "Luke", "Steve", "John")

# *********************passing list as argument in function******************************
def multiply(num):
    print(type(num))
    m=1
    for i in num:
        m=m*i
    return m
print(multiply([1,2,3,4,5,6,7,8,9]))

#  **************************************************recursion******************

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

def sum(x):
    if x==1:
        return 1;
    else:
        return (x+sum(x-1))
num=5
print("sum is :",sum(num)) 


def squaresum(x):
    if x==1:
        return 1;
    else:
         
        return (x*x+squaresum(x-1))
num=5
print("sum is :",squaresum(num))


# *********************************************local , global , non local keywords**********************************
# if we dont use gloabal keyword inside inside the function then we can only read the global variable and cannot write it
c = 1 # global variable

def add():
    print(c)  # valid

add()   

# invalid 
c = 1 # global variable
    
def add():
    #c = c + 2 # increment c by 2
    print(c)

add()


# solution of this problem

c =  4 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)



# global in nested function


def foo():
    x = 20

    def bar():
        global x
        x = 25       # we can even declare a global variable inside nested function
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)


#*******************************************      local variable***********************************8


# local variable is the varible declared  inside the function we cannot access local variables outside function scope

def foo():
    y = "local"
    print(y)

foo()

x = "global "

def foo1():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo1()


# ************************************************* non-local keyword************************


# non local keyword is used inside the nested function to access the local variable

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
