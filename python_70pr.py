"""
******************1******************
a=float(input("enter a float number"))
print("{:.2f}".format(a));

"""
"""
****************2************88
b=lambda x,y: x*y
print(b(10,10))

"""
"""
****************3***********

import math
c=lambda r:(4/3)*math.pi*r*r*r
print(c(10))

"""

"""
***********4 ,5 ******************

a1=float(input("enter 1 number \n"))
a2=float(input("enter 2 number \n"))
a3=lambda x,y:x*y
a4=lambda x:x+x*x+x*x*x
print(a3(a1,a2))
print(a4(a1))


"""

"""
******************6*****************
def l(s):
    count = 0
    for char in s:
        count += 1
    return count
print(l('tushar sharma'))


"""

"""
*******************7*************8
s = "1500.376"
print(int(s))
print(float(s))

"""

"""
****************8****************
def sum(a,b):
    s=a+b
    if(s>100):
        return s
    else:
        return a*b

sum(10,20)

"""


"""

****************9****************

def ran(a,b,c):
    s=a+b+c
    if(a==b and a==c):
        return s
    else:
        return s*4
ran(12,13,14)

"""

"""
****************10****************


def dis(co)
    if(co>10000):
        print("you have got 50 percent discount now cost=",co/2)


q=int(input("enter the quantity of items: "))
c=q*100

dis(c)

"""

"""
****************11****************


def div(num):
    if(num%8==0):
        print("divisible by 8")
        if(num%12==0):
          print("divisible by 12")
    else:
        print("divisible by none")

div(24)

"""

"""

****************12****************


def evod(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")

evod(3)

"""

"""
****************13****************


sub1=int(input("Enter marks of the physics subject: "))
sub2=int(input("Enter marks of the chemistry subject: "))
sub3=int(input("Enter marks of the biology subject: "))
sub4=int(input("Enter marks of the maths subject: "))
sub5=int(input("Enter marks of the computer subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80):
    print("Grade: B")
elif(avg>=70):
    print("Grade: C")
elif(avg>=60):
    print("Grade: D")
elif(avg>=40):
    print("Grade: E")
else:
    print("Grade: F")



"""

"""

****************14****************



per=int(input("enter the number of persons: "))
li=[]
for i in range(per):
    li.append(int(input("enter the age: ")))
li=sorted(li)
print("oldest: ",li[-1])
print("youngest: ",li[0])

"""

"""
****************15****************



def bill(units):
    amount=0;
    while(units!=0):
        temp=0
        if(units>250):
            temp=units-250
            units=250
            amount+=temp*1.5
        elif(units>150):
            temp=units-150
            units=150
            amount+=temp*1.2
        elif(units>50):
            temp=units-50
            units=50
            amount+=temp*0.75
        elif(units>=0):
            amount+=units*0.5
            units=0

    amount=amount+amount/5
    return amount

u=float(input("ENTER THE UNITS CONSUMED: "))
print("amount to be paid is: "bill(u))





        """

"""****************************16*************************
classheld=int(input("enter no. of classes held: "))
classattended=int(input("enter the classes attended: "))
attendper=(classattended*100)/classheld
if(attendper>80):
    print("can give exam attendence is {:4.2f}% ".format(attendper))
else:
    print("cannot give exam attendence is {:4.2f}%".format(attendper))

"""

"""
*******************17********************
income=int(input("enter the income"))
tax=0
if(income<100000):
    print("tax to be paid: ",tax)
elif(income>100000 and income<200000):
    tax=income*0.1
    print("tax to be paid: ",tax)
else:
    tax=income*0.2
    print("tax to be paid: ",tax) 




"""  

"""
***********************18******************

num=int(input("enter the number: "))
temp=0
sum=0
while(num!=0):
    temp=num%10
    sum=sum+temp
    num=num//10
print("digital sum is given by ",sum)

"""

"""
*********************19*************************

num=int(input("enter the number: "))
temp=0
product=1
while(num!=0):
    temp=num%10
    product=product*temp
    num=num//10
print("digital product is given by ",product)



"""

"""
**********************************20***************************

n=int(input("enter the no. of terms: "))
sum=(10**(n+1)-10-9*n)/27
print(sum)

"""


"""
****************************21***********************

n=int(input("enter rows "))
r=n//2
for i in range(r):
      print("*"*(i+1))
for i in range(r):
    print("*"*(r-i))

"""
"""
 ************22***************************88

n=input("enter the number")
print(n[::-1])


"""

"""
****************************23***************************
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
"""
"""
**************************************24********************************


num = 1634

 
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

"""

"""
*******************25************

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
"""

"""
****************************************26*********************

import math  
num = int(input(" Enter the Number:"))  
sum = 0  
temp = num  
  
while(temp > 0):  
    rem = temp % 10  
    fact = math.factorial(rem)  # Using the buitlt-in factorial() function  
  
    print("Factorial of %d = %d" %(rem, fact))  
    sum = sum + fact  
    temp = temp // 10  
  
print("\n Sum of Factorials of a Given Number %d = %d" %(num, sum))  
      
if (sum == num):  
    print(" The given number is a Strong Number")  
else:  
    print(" The given number is not a Strong Number")   

"""

"""
**********************************27***************************
"""

"""
**********************************28***************************

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
"""

"""
**********************************29***************************

num = int(input("Enter a number: "))
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
"""

"""
**********************************30***************************

rows = int(input("Enter the number of rows: "))  
  
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  
"""

"""
**********************************31***************************

rows = int(input("Enter the number of rows: "))   
for i in range(rows+1):  
  
    for j in range(i):  
        print(i, end=" ")  # print number  
    print(" ")  
"""

"""
**********************************32***************************

rows = int(input("Enter the number of rows: "))  
  
for i in range(1, rows+1):  
    for j in range(1, i + 1):  
        print(j, end=' ')  
    print("")  
"""

"""
**********************************33***************************

n = int(input("Enter number of rows: "))

a = 97

for i in range(1,n+1):
    for j in range(1, i+1):
        print("%c" %(a), end="")
    a +=1
    print()
"""

"""
**********************************34***************************

str = input("Enter a string: ")

counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)
"""

"""
**********************************35***************************

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))
"""

"""
**********************************36***************************

def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'polis':
      str1 += 'poliscs'
    else:
      str1 += 'polis'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
"""

"""
**********************************37***************************

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))
"""

"""
**********************************38***************************

def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('abcd'))
print(change_sring('12345'))
"""

"""
**********************************39***************************

def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))
"""

"""
**********************************40***************************

user_input = input("What's your favourite language? ")
print("My favourite language is ", user_input.upper())
print("My favourite language is ", user_input.lower())
"""


"""
*******************************************41************************

str1 = 'The quick brown fox jumps over the lazy dog.'
print()
print(str1.count("fox"))
print()



"""

"""
*******************************************42************************

str1 = 'Tushar sharma'
print(str1[:4].lower() + str1[4:])



"""

"""
*******************************************43************************
def remove_spaces(str1):
  str1 = str1.replace(' ','')
  return str1
    
print(remove_spaces("T u s ha r"))
print(remove_spaces("S ha r ma "))


"""

"""
*******************************************44************************

def moveSpaces(str1): 
    no_spaces = [char for char in str1 if char!=' ']   
    space= len(str1) - len(no_spaces)
    result = ' '*space    
    return result + ''.join(no_spaces)
  
s1 = "T us har shar m a"
print("Original String:\n",s1)

print("\nAfter moving all spaces to the front:")
print(moveSpaces(s1))


"""

"""
*******************************************45************************

from collections import Counter

string= "pppppppghhhijeuupffe"
print(string)

result= Counter(string)
result= max(result, key=result.get)

print("Most frequent character: ",result)



"""

"""
*******************************************46************************

def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  
     
print(capitalize_first_last_letters(" tushar sharma"))
print(capitalize_first_last_letters(" acropolis college"))




"""

"""
*******************************************47************************
def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit
     
print(sum_digits_string("123abcd45"))
print(sum_digits_string("abcd1234"))


"""

"""
*******************************************48************************

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["tushar", "krishna", "harsh"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])

"""

"""
*******************************************49************************
def x(n):
    return n^2 + 1

print x(4)


"""

"""
********************************************60***********************
 str = 'Y-tatata-acropolis: 0.8475'
 start = str.find(':')
 print(start)
 number = str[start+1:]
 new_number = float(number)
 print ('Number:',number,type(number))
 print ('New Number:',new_number,type(new_number))


"""

"""
*******************************************65************************

a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median is", median)

"""

 
"""
*******************************************66************************
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


"""

"""
*******************************************67************************
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


"""

"""
*******************************************68************************

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))

"""

"""
*******************************************69************************

num = 163486
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

"""

"""
*******************************************70************************
def B():
    print("Inside the method B.")
    
def A():
    print("Inside the method A.")
    return B

returned_function = A()
returned_function()


"""

 


list1 = [11, 5, 17, 18, 23]
 
total = sum(list1)
print("Sum of all elements in given list: ", total)
"""
"""
 