#Error Handling

#No Error Occured
number1=0
number2=20
x=(number1/number2)
print(x)
print("Programme Ended")

#Error Occurs
number1=0
number2=20
try:
    x=(number2/number1)
    print(x)
except:
    print("An Error Occured")


print("Programme Ended")


#Exception Tells You What Exactly Went Wrong
number1=0
number2=20
try:
    x=(number2/number1)
    print(x)
except Exception as r:
    print("An Error Occured",r)


print("Programme Ended")
#Else :This Is Executed When The Try Does Not Apply
number1=0
number2=20
try:
    x=(number2/number1)

except Exception as r:
    print("An Error Occured",r)


print("Programme Ended")

"""
else:
    print(x)
    print("All Is Well")
"""