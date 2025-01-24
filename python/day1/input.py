# input = we use input function as a prompts so that user ent the data 
#        return the entered data as a string.
name = input("what is your name?")
age =  input("how old are you?")

age= int(age)#yeha chai str lai int ma change gareko

age = age + 1

print (f"hellow {name}!")
print(f"you are {age} years old")
print(f"happy birthday {name}")