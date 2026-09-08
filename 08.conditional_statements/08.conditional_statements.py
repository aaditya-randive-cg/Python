#a basics of 
#question1
number=int(input('Enter the number'))
if number >10:
    print("Greater than 10")

#question2
person=int(input("Enter Age"))
if person >= 18:
    print("Adult")

#question3
number=int(input('Enter the number'))
if number >0:
    print("positive")

#question4
marks=int(input("Enter marks"))
if marks>=40:
    print("pass")

#question5
number=int(input('Enter the number'))
if number==0:
    print("Zero")

#question6
number=int(input('Enter the number'))
if number<0:
    print("Not positive")
if number<0 or number==0:
    print("positive")

#question7
number=int(input("Enter number"))
if  number<18:
    print("Adult")
else:
    print("Minor")

#question8
number=int(input("Enter number"))
if number %2==0:
    print("even")
else:
    print("odd")

#question9
marks=int(input("Enter number"))
if marks>=40:
    print("pass")
else:
    print("fail")

#question10
number1=int(input("Enter "))
number2=int(input("Enter"))
if number2>number1:
    print("number2 is greater")
if number1>number2:
    print("number1 is greater")
else:
    print("equal")

#question11
marks=int(input("Enter "))
if marks>=90:
    print("A")
elif marks>75 and marks<89:
    print("B")
elif marks >60 and marks<74:
    print("C")

elif marks>40 and marks<59:
    print("D")
else:
    print("F")


#question12
number=int(input("number"))
if number>0:
    print("Positive")
if number<0:
    print("negative")
else:
    print("zero")

#question13
number=int(input("number"))
if number==1:
    print("Monday")
elif number==2:
    print("Tuesday")
elif number==3:
    print("Wednesday")
elif number==4:
    print("Thursday")
elif number==5:
    print("Friday")

#question14
marks=int(input("enter "))
if marks>=90:
    print("Excellent")
elif marks>75 and marks<89:
    print("Good")
elif marks >60 and marks<74:
    print("Pass")


else:
    print("F")

#question15
number=int(input("enter "))
if number==1:
    print("1")
elif number==2:
    print("2")
elif number==3:
    print("3")
else:
    print("error")

#question16
person=int(input("Enter"))
if person>=18:
    if person>=60:
        print("Between 18 and 60")

#question17
mark=int(input("Enter"))
if mark>=40:
    if mark>=75:
        print("Good")
    else:
        print("Passed")
else:
    print("fail")

#question18
number=int(input("Enter"))
if number>0:
    if number>100:
        print('number is positive greater than 100')

#question19
age=int(input("Enter age"))
if age>=18:
    print("18")
    if age<=60:
        print("at")

#question20
number=int(input("enter"))
if number !=0:
    print("non-zero ")
    if number>0:
        print("Positive")
    else:
        print("Negative")

#question21
marks=int(input('Enter marks'))
age=int(input("Enter age"))
if age>=18 and  marks>=40:
    print("Eligible")

#question22
number=int(input("number"))
if number < 10 or number > 100:
    print("Special")

#question23
age=int(input("Enter"))
has_id=bool(input("Enter"))
if age >= 18  and has_id==True:
    print("Allowed")

#question24
firstnumber=int(input("Enter Number1"))
secondnumber=int(input("Enter Number2"))
if firstnumber > 10 and secondnumber > 10:
    print("Both are greater then 10")

#question25
number=int(input("Enter "))
if number<0  or  number>100:
    print("less then 0 greater then 100")

#question26
is_closed = False

if not is_closed:
    print("Open")
    
#question27
num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Between 10 and 50")

#question28
num = int(input("Enter a number: "))

if num < 10 or num > 50:
    print("Outside the range")

#question29
is_student = True
has_id = True
has_ticket = True

if is_student and has_id and has_ticket:
    print("Allowed")

#question30
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
has_id = input("enter") == "True"

if age >= 18 and marks >= 40 and has_id:
    print("Eligible")
else:
    print("Not eligible")