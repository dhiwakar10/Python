name = "jack"

def mydata():
    print("my data is", name)

    def myname():
        print("my name is", name)
        
        
        mydata()
        myname()
        print(name)
def myname():
    name = "Dhiwa"
    print("my name is", name)

def myage():
    age =20
    print("my age is", age)

def myphone():
    phone =9080070700
    print("my phone number", phone)
        

myname()
myage()
myphone()

# a=int(10)
print(a)

a=int(10.100)
print(a)

a=int("10")
print(a) 

#a=float(10)
print(a)
a=float(True)
print(a)
print(float(False))

# a=complex(10)
print(a)
a=complex(10.272)
print(a)
a=complex("10")
print(a)
a=complex("10.272")
print(a)

#a=str(10)
print(a)
a=str(10.272)
print(a)
a=str("10")
print(a)
a=str("10.272")
print(a)
a=str("jack123")
print(a)
a=str(3+2j)
print(a)

# a=bool(10)
print(a)
a=bool(10.272)
print(a)
a=bool("10")
print(a)
a=bool("10.272")
print(a)
a=bool("jack123")
print(a)
a=bool(3+2j)
print(a)

# x="python"

def myprogramme():
    global x
    x="java"
    print(x)

myprogramme()
print("'python' is a programming language")
print('"java" is a programming language')

#######
def myName(name):
    print("my name is",name)

def myAge(age,DOB):
        print("my age is",age)
        print(DOB)
myName("Bhuvi")
myAge(20,"11/04/2003")
 
        #######
def votingEligiblity(age):
    if age>=18:
      print("Eligible to vote")

votingEligiblity(20)


def subject(maths):
   if maths>=50:
      print("You Pass the Maths Exam")
   else:
      print("You Fail the Maths Exam")

subject(70)


def  number(even):
   
   if even %2==0:
      print("It is an Even Number")
   else:
      print("It is an Odd Number")

n=int(input("Enter the value"))
number(n)

def bloodDonatation(age,weight):
    if age>=20  and weight>=55:
        print("Eligible to Donate the Blood")
    else:
        print("Not Eligible to Donate the Blood")

a=int(input("Enter the age:"))
b=int(input("Enter the weight:"))
bloodDonatation(a,b)

 #### Nested for loop
for i in range(1,4,1):
    for j in range(1,4,1):
        print(i) 

#######
x=["java","python", "c#", "java"]
print(x)

for i in x:
    print(i)

print(x[i])


d=["java",10,"python", 10, True,98.93 ,10]
print(d)

print(d.index (10))
print(d.index(10,2))
print(d.index(10,2,5))

d1=[100,201,420,45,10]
mini=min(d1)
print(mini)
maxi=max(d1)
print(maxi)

newlist=d.copy()
print(newlist)

###### Inheritance
class Teacher:

    def teacherName():
        print("jack")

class Student(Teacher):

    def studentName():
        print("Max")

class Address(Student):

    def location():
        print("chennnai")

a=Address()
a.studentName()
a.location()
a.teacherName()
