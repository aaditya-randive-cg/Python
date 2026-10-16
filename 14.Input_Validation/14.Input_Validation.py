# #A
# #question1
# marks = int(input("Enter marks  "))
# while marks < 0 or marks > 100:
#     print("Invalid")
#     marks = int(input("Enter marks  "))
# print("Accepted marks", marks)

# #question2
# number=int(input("Enter number"))
# while number<=0:
#     print("invalide")
#     number=int(input("Enter number"))
#print("accepted")

# #question3
# age=int(input("Enter age"))
# while age<0 or age>120:
#     print("invalide")
#     age=int(input("Enter age"))
# print("accepted")

# #question4
# choice=int(input("Enter choice"))
# while choice!=1 and choice!=2 and  choice!=3 and  choice!=4 and  choice!=5:
#     print("invalide")
#     print('''1. View profile
# 2. Edit profile
# 3. Settings
# 4. Exit''')
    
#     choice=int(input("ENTER CHOICE"))
# else:
#     print("ACCEPT")

# #question5
# password=int(input("ENTER PASSWORD"))
# while password<8:
#     print("invalid password")
#     password=int(input("ENTER PASSWORD"))
# else:
#     print("validpassword")

#question6
temp=int(input("ENTER TEMPERATURE"))
while temp<-20 or   temp>45:
    print("invalid")
    temp=int(input("ENTER TEMPERATURE"))
else:
    print("valide")
# a=10
# b=20
# c=40
# def add(a,b):
#     c=a+b 
#     return c


# def sub(a,b):
#     return a-b


# def mul(a,b):
#     return a*b

# result=sub(add(a,b),c)
# print(result)
# print(mul(sub(add(a,b),c),a))
# print(mul(sub(a,b),add(b,c)))

def introduce(name, age):
    print(name, age)

introduce(name="Asha", age=21)
