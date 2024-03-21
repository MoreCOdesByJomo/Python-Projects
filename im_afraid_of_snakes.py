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
"""

"""
#loops
#the while loop...
x=1
while x<5:
 if x==3:
    break
    print(x)
    x+=1
"""

"""
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

"""
my_name=input("enter your name")
print("Your name is",my_name)
"""

"""
name=list()
fir_name=input("enter your first name")
sec_name=input("enter your second name")
third_name=input("enter your third name")
print("Your name is",fir_name,sec_name,third_name)
"""

"""
#tuples
fruits = ( "apple", "banana", "mangoes")
print(fruits)
print(fruits[2])
#if I want to modify a tuple
# convert tuple into a list
# make your changes
# revert list back to tuple

#How to change from tuple to list
myfruitslist=list(fruits) #converting a tuple into a list
print(myfruitslist)
myfruitslist[2]="pineapples" #modifying the list
print(myfruitslist)
fruits=tuple(myfruitslist) #converting the list back to a tuple
print(fruits)
#fruits[2]="pineapples"
#print(fruits)

#dictionary
cardict ={
    "brand":"Ford",
    "model":"Mustang",
    "year": 1986
}

print(cardict[ "year"])
"""

#creating a function
"""
def printJomo(x):
    for i in range(1,11):
     print(x)

#making a call to a function
#for i in range (100):
printJomo("zooweee")


#function for modulus
def getModulus(x,y):
    return x%y


print(getModulus( 5,  2))
"""




#LISTS     QUESTION2:Write A Program That Outputs The Repeated Elements In A List

listz=["cheese","tomato","potato","tomato","ram","ram"]
repeated_veg=set()
unrepeated_veg=[]
for item in listz:
    if listz.count(item)>1:
        repeated_veg.add(item)
    else:
        unrepeated_veg.append(item)


print("The repeated item is",repeated_veg)
print("The unrepeated item is",unrepeated_veg)





#TUPLES      QUESTION1:Write A Program That Adds Items To A Tuple


pyfruit = ("apple", "banana", "cherry")
print(pyfruit)
def additems(x):
    y = list(pyfruit)
    y.append(input("Fruit To Be Added: "))
    pyfruits = tuple(y)
    print(pyfruits)
additems(x)





#DICTIONARY    QUESTION1:Write A Program That Deletes A List Of Keys From A Dictionary


mydict={"brand":"Toyota","model":"Haarrier","year":2016}



#Solution 2
mydict={"brand":"Toyota","model":"Haarrier","year":2016}
print("Koech :My Old Dictionary Is",mydict)
del mydict["year"], mydict["brand"]
print("Koech : My New Dictionary Is",mydict)
#DICTIONARY QUESTION2:Write A Program That Checks If A Value Exists in A Dictionary

"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
def valuecheck(x):
    input("Check If Value Is Present: ")
    if input==["Ford"] or input==["Mustang"] or input==[1964]:
       print("Present")
    else:
        x +=(input)
        print("Added")
        print(x)

"""


#Erro Handling
number1=1
number2=20

x=number1/number2
print(x)
print("Programme Ended")
























