# write a program to find the greatest of four numbers entered by a the user
a1= int(input("enter the first number"))
a2=int(input("enter the second number"))
a3=int(input("enter the third number"))
a4=int(input("enter the fourth number"))

if (a1>a2 and a1>a3 and a1>a4):
    print('a1 is the greatest number:',a1)
elif (a2>a1 and a2>a3 and a2>a4):
    print('a2 is the greatest number',a2)
elif (a3>a1 and a3>a2 and a3>a4):
    print("a3 is the greatest number",a3)
