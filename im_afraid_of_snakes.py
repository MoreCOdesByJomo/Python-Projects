#single line comment
"""
multi line comment
bluh bluh bluh
bluh bluh bluh
"""

#variables
student_name = "Jomo" #string
student_age =17 #integer
student_fees =100.0 #float
is_male=True #boolean
print(student_name,student_age,student_fees)
#the above lack prints

x=y=z=10 #assigning one value to multiple variables
x,y,z=5,10,11 #assigning multiple values to multiple variables

#case sensitivity
STUDENT_NAME = "James"
student_name = "Jonas"
print(STUDENT_NAME)

print(student_name)

price= 10
quantity= 5
total_price= price+quantity
myanswer1="total is: "+str(total_price)+" Kenya shillings"
myanswer2="the total is: ",total_price," kenya shillings"

#print("the total is: "+str(total_price)+"Kenya shillings")


#LOGICAL_operator
age=20
nationality= "Rwanda"

if nationality =="kenyan" and  age>=35:
    print("you can be president")
else:
    print("you cannot be president")

age =17
constituency= "Embakasi"

if constituency=="Westlands" or "Kasarani" or "Westlands" and age>=18:
    print("you can be Governor Of Nairobi")
else:
    print("you cannot be Governor Of Nairobi")
