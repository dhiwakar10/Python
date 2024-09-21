def subject(maths):
   if maths>=50:
      print("You Pass the Maths Exam")
   else:
      print("You Fail the Maths Exam")

subject(70)

#######

def  number(even):
   
   if even %2==0:
      print("It is an Even Number")
   else:
      print("It is an Odd Number")

n=int(input("Enter the value"))
number(n)

############

def bloodDonatation(age,weight):
    if age>=20  and weight>=55:
        print("Eligible to Donate the Blood")
    else:
        print("Not Eligible to Donate the Blood")

a=int(input("Enter the age:"))
b=int(input("Enter the weight:"))
bloodDonatation(a,b)