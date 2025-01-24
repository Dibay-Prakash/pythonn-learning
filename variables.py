# variable behaves as if it was the value it contains 

first_name = "dibas"
food = 'pizza'

print(f" hellow {first_name}")
#f means a format in the python
print (f"you like {food}?")

#integers
# integers is a whole number, positive or negative ,without decimals of 
#unlimte length.
age = 25
quantity = 5
sem = 6

print (f"you are {age} years old")
print (f"you are buying {quantity} items from my stores of shoe")
print (f"currently i study in semester {sem} th.")

# float
#The FLOAT data type stores double-precision floating-point
#  numbers with up to 17 significant digits.
price = 10.99
gpa = 4.0
distance = 4.5

print(f"the price of the topi is {price}")
print (f"i wish i had {gpa} ")
print (f"the distance from my flat to sirish room is {distance}km")

#Boolean
#Boolean is just another data type similar to integers and strings. 
# However, Boolean variables can have only two values: True and False

is_student = True

if is_student:
    print("you are a student")
else:
    print("your are Not a student")
