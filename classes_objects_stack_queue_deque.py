#**********************************  stack*******************************

class Stack: 
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
        return data 
    
    def pop(self): 
        return self.elements.pop() 
        
    def peek(self): 
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0

if __name__ == '__main__':
    stack = Stack()
    
     
    print(stack.is_empty())

   
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    
    print(stack.is_empty())

     
    print(stack.peek())

   
    stack.pop()

 
    print(stack.peek())

   
    stack.pop()
    stack.pop() 
    stack.pop() 
    stack.pop() 

 
    print(stack.is_empty())

#**************************************queue******************************************

class Queue:

	def __init__(self):
		self.elements = []

	def enqueue(self, data):
		self.elements.append(data)
		return data

	def dequeue(self):
		return self.elements.pop(0)

	def rear(self):
		return self.elements[-1]

	def front(self):
		return self.elements[0]

	def is_empty(self):
		return len(self.elements) == 0

if __name__ == '__main__':
	queue = Queue()

 
	print(queue.is_empty())

	 
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	queue.enqueue(4)
	queue.enqueue(5)
 
	print(queue.is_empty())

	 
	print(queue.front(), end=' ')
	print(queue.rear())

 
	queue.dequeue()

	 
	print(queue.front(), end=' ')
	print(queue.rear())

 
	queue.dequeue()
	queue.dequeue()
	queue.dequeue()
	queue.dequeue()
	print(queue.is_empty())

#**************************************dequeue***************************************************

class Dequeue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def append(self, data):
        self.items.append(data)
 
    def append_left(self, data):
        self.items.insert(0, data)
 
    def pop(self):
        return self.items.pop()
 
    def pop_left(self):
        return self.items.pop(0)
    def show(self):
        print(self.items[:])
 
 
q = Dequeue()
print('Menu')
print('append <value>')
print('appendleft <value>')
print('pop')
print('popleft')
print('quit')
print('show')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'append':
        q.append(int(do[1]))
    elif operation == 'appendleft':
        q.append_left(int(do[1]))
    elif operation == 'pop':
        if q.is_empty():
            print('Dequeue is empty.')
        else:
            print('Popped value from right: ', q.pop())
    elif operation == 'popleft':
        if q.is_empty():
            print('Dequeue is empty.')
        else:
            print('Popped value from left: ', q.pop_left())
    elif operation == 'quit':
        break
    elif operation=='show':
        q.show()






# class programs 

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

print(blu.sing("'Happy'"))
print(blu.dance())


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
  
 
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
  
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
  
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


class Bird:
    
    def intro(self):
        print("There are many types of birds.")
  
    def flight(self):
        print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly.")
  
class ostrich(Bird):
  
    def flight(self):
        print("Ostriches cannot fly.")
  
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()

 
  
class Person1:

	 
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
	
# child class
class Employee(Person1):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person1.__init__(self, name, idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))


a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()


class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
  
# Creating a derived class
class Derived(Base):
    def __init__(self):
  
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
  
  
# Driver code
obj1 = Base()
print(obj1.a)


class Person2:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# create a new object of Person class
harry = Person2()

# Output: <function Person.greet>
print(Person2.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.greet)

# Calling object's greet() method
# Output: Hello
harry.greet()


class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
print(num1.attr)

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()

t.inputSides()

t.dispSides()

t.findArea()

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
 
# Driver Code       
t = Test(1234, 5678)
print(t)

class Base(object):
    pass   # Empty Class
  
class Derived(Base):
    pass   # Empty Class
  
# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))
  
d = Derived()
b = Base()
  
# b is not an instance of Derived
print(isinstance(b, Derived))
  
# But d is an instance of Base
print(isinstance(d, Base))


class Base1:
    def __init__(self):
        self.str1 = "Geek1"
        print ("Base1")
  
class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"        
        print ("Base2")
  
class Derived(Base1, Base2):
    def __init__(self):
          
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
          
    def printStrs(self):
        print(self.str1, self.str2)
         
  
ob = Derived()
ob.printStrs()



 


   
