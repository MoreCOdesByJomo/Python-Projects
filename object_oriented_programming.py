"""
class Student:
    student_name=''
    student_age=0
    student_marks=0
    def __init__(self):#First Function Is A Constructor
        print("Constructor Called")

    def set_student_name(self,name):#Second Function Takes The Parameter Name And Sets It To The Property
        self.student_name=name

    def display_student_name(self):#Third Function Displays The Student Name
        print("Student:",self.student_name)

student1=Student()
student1.set_student_name("jomo")
student1.display_student_name()
"""

"""
class student:
    student_name=''
    student_age=0
    student_marks=0
    def __init__(self):
        print("Constructor Called")

    def set_student_age(self,age):
        self.student_age=age

    def set_student_name(self,name):
        self.student_name=name

    def display_student_age(self):
        print("Student:",self.student_age,self.student_name)

student1=student()
student1.set_student_name("jomo")
student1.set_student_age(20)
student1.display_student_age()
"""

#Program With Parameters:This Is Much Easier
class student:
    student_name=''
    student_age=0
    student_marks=0
    def __init__(self,name,age):
        self.student_name=name
        self.student_age=age
        print("Constructor Called")

    def display_student_details(self):
        print("Student:",self.student_age,self.student_name)

student0=student("Joe",22)
student0.display_student_details()










































