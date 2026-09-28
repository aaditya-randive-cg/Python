#question1
number=int(input("Enter number"))
if number>0:
    print("Positive")
elif number<0:
    print("Negetive")
else:
    print("Zero")

#question2
numbe=int(input("Enter number"))
if number>0 and number%2==0:
    print("Positive Even")
elif number>0 and number%2!=0:
    print("Positive Odd")
elif number<0 and number%2==0:
    print("Negative Even")
elif number<0 and number%2!=0:
    print("Negative Odd")
else:
    print("Zero")

#question3
number1=int(input("Enter number1"))
number2=int(input("Enter number2"))
if number1>number2:
    print("Number1 is Greater than Number2")
elif number2>number1:
    print("NUmber2 is Greater then Number1")
else:
    print("same ")

#question4
number1=int(input("Enter number1"))
number2=int(input("Enter number2"))
number3=int(input("Enter number3"))
if number1<number2 and number1<number3:
    print("number1 is smalleat")
elif number2<number1 and number2<number3:
    print("number2 is samllest")
elif number3<number2 and number3<number1:
    print("number3 is smallest")

#question5
number1=int(input("Enter number1"))
number2=int(input("Enter number2"))
number3=int(input("Enter number3"))
if number1>number2 and number1>number3:
    print("number1 is largest")
elif number2>number1 and number2>number3:
    print("number2 is largest")
elif number3>number2 and number3>number1:
    print("number3 is largest")

#question6
number=int(input("Enter Number"))
if number%11==0 and number%5==0:
    print("Divisible by 11 and 5")
elif number%5==0:
    print("Divisible by only 5")
elif number%11:
    print("Divisible by only 11")
else:
    print("divisible by no")

#question7
number=int(input("Enter number"))
if number%3==0 and number%7==0:
    print("Divisible n=both 3 and 7")
elif number%3==0:
    print("Divisible by 3")
elif number%7==0:
    print("Divisible by 7")
else:
    print("Divisible no")

#question8
marks=int(input("Enter Marks"))
if marks<0 or marks>100:
    print("Invalid ")
elif marks>=40:
    print("Pass")
elif marks<40:
    print("Fil")

#question9
marks=int(input("Enter Marks"))
if marks>=90 and marks>=100:
    print("A")
elif marks>=89 and marks>=80:
    print("B")
elif marks>=70 and marks>79:
    print("C")
elif marks>=60 and marks>=69:
    print("D")
elif marks>=40 and  marks>=59:
    print("E")
elif marks<40:
    print("Fail")

#question10
age=int(input("Enter age"))
if age<=0:
    print("Invalid")
elif age<18:
    print("Cannot vote")
elif age<=18:
    print("camn vote")

#question11
year=int(input("Enter Year"))
if year%400==0 or (year%4==0 and year%100==0):
    print("leap year")

#question12
string=input("Enter string")
if string 


#question13
character=input("Enter character")
if character== "A " or "E" or "I" or "O" or "U" or "a" or "e" or "i" or "o" or "u"  :
    print("vovel")
elif character

#question14
cost_price=int(input("Enter cost"))
selling_price=int(input("Enter selling"))
if cost_price<selling_price:
    print("Profit")
elif selling_price<cost_price:
    print("Loss")
else:
    print("no profit no loss")

#question15
cost_price=int(input("Enter cost"))
selling_price=int(input("Enter selling"))
profit=selling-price-cost_price
loss=cost_price-selling_price
profit_perc=profit/cost_price*100
loss_perc=loss/cost_price*100
print("loss_perc",loss_perc)
print("profit_perc",profit_perc)

#question16
bill=int(input("Enter bill"))








#question17
number1=int(input("Enter Number1"))
number2=int(input("Enter Number2"))
operator=input("Enter operay")
if operator=="+":
    print(number1+number2)
elif operator=="-":
    print(number1-number2)
elif operator=="*":
    print(number1*number2)
elif operator=="/":
    if number2!=0:
        print(number1/number2)
    else:
        print(" ZERO ERROR")

#question18
temprature=int(imput("Enter tenperature"))
if temprature<0:
    print("Freesing")
elif temprature>=0 and temprature<=15:
    print("very cold")
elif temprature>=16 and temprature<=25:
    print("cold")
elif temprature>=26 and temprature<=35:
    print("number")
else:
    print("Hot")

#question19
number=int(input("ENter number"))
if number<0:
    print("negative")
elif number>0 and number<=10:
    print("number is between 0-10")
elif number>=11 and number>=50:
    print("number is between 11-50")
elif number>=51 and number<=100:
    print("number is between 51-100")
else:
    print("above 100")

#question20
first_side=int(input("Enter 1side"))
second_side=int(input("Enter 2side"))
third_side=int(input("Enter 3side"))
if first_side+second_side>third_side or first_side+third_side>second_side or second_side+third_side>first_side:
    print("valid triangle")

#question21
first_side=int(input("Enter 1side"))
second_side=int(input("Enter 2side"))
third_side=int(input("Enter 3side"))
if first_side+second_side>third_side or first_side+third_side>second_side or second_side+third_side>first_side:
    print("valid triangle")
    if first_side==second_side==third_side:
        print("Equilateral")
    elif first_side==second_side or first_side==third_side or third_side==second_side:
        print("Isosecle")
    elif first_side!=second_side!=third_side:
        print("scalene")

#question22
account=float(input("Enter accountbalance"))
withdrawal=float(input("Enter  withdrawal"))
if withdrawal>0:
    if withdrawal%100:
        if account>withdrawal:
            if account>=500:
                print("withdeawal succesful")


#question23
