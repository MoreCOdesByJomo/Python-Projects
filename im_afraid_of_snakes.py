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



pen=60.0
books="50"
total = pen+float(books)
result="my total is "+str(total)+" Kenya shillings"
print(result)
#print("the total is",total)

y=100
x=2
ans=y%x
if ans==0:
    print("y is an even number")
else :
    print("y is an odd number")




"""
#y =int(input("enter your number here"))
x = 2
ans = y % x
if ans == 0:
    print("y is an even number")
else:
    print("y is an odd number")



#loops
#the while loop...
x=1
while x<5:
 if x==3:
    break
    print(x)
    x+=1

y=1
while y<5:
    y+=1
    if y==3:
        continue
        print(y)
        y+=1

"""

"""
country=input("enter your country")
if country=="Kenya":
    print("Free Trade Accepted")
elif country=="Tanzania":
    print("Free Trade Accepted")
elif country=="Uganda":
    print("Free Trade Accepted")
elif country=="S.Sudan":
    print("Free Trade Accepted")
else:
    print("Free Trade Denied")
"""

"""
x=1
while x<=10:
    if x==3 or x==5:
        x+=1 #this is used for the increment
        continue
    print("the number is",x)
    x+=1
"""


total=0
number=1
while number<=10:
    total +=number
    number+=2
    print("the sum of odd numbers is",total)

#For Loop
"""Dogs=("pup","pug","German Shepherd")
for x in Dogs:
    print(x)
"""


"""for x in range(1,10,2):
    print(x+x+x+x+x)
    """


total=0
for num  in range(1,11,2):
    total+=num
    print("The sum of odd numbers of",total)

sum_odd=0
for i in range(10):
    if i%2!=0:
        sum_odd +=1
print("The sum of odd numbers",sum_odd)

#List(A variable that holds a number of items)
"""
my_students=list()#empty list
my_stationery=["pens","books","pencils"]
print(my_stationery)
my_stationery.append("files")
print(my_stationery)
my_stationery[0]="booksupdated"
print(my_stationery)
"""

my_name=input("enter your name")
print("Yourname is",my_name)



