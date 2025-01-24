# typecasting  is the process f converting a variable form one data type to another
#str(), int(),float(),bool()
#type casting is heavily used for handling user input because user input is always in str()

name = "dibay"
age = 25
gpa=3.6
is_student = True

gpa = int(gpa)#here the floating point value 3.6 stored in gpa to an integer
#the int() function truncates the decimal part so 3.6 becomes 3.

print (gpa)

name = bool(name)
print (name)