a=int(10)
print(a)

a=int(10.100)
print(a)

a=int("10")
print(a) 

##Float
a=float(10)
print(a)
a=float(True)
print(a)
print(float(False))


##Complex
a=complex(10)
print(a)
a=complex(10.272)
print(a)
a=complex("10")
print(a)
a=complex("10.272")
print(a)

##String
a=str(10)
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

##Boolean

a=bool(10)
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

x="python"

def myprogramme():
    global x
    x="java"
    print(x)

myprogramme()
print("'python' is a programming language")
print('"java" is a programming language')
