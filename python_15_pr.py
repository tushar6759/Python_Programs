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
  




