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
