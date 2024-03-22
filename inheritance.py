class person: #superclass or parent class
    name=""
    age=""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvehicle(self):
        print("The details of the vehicle are",self.name,self.age)
class student(person):
    def __init__(self,name,age):
        super().__init__(name,age)

