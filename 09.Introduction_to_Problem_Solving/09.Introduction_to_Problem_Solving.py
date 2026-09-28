# #question1
# number=int(input("Enter number"))
# if number<0:
#     print("negative")
# elif number>0:
#     print("positive")
# else:
#     print("Zero")

# #question2
# number=int(input("Enter number"))
# if number>0 and number%2==0:
#     print("Positive Even")
# elif number>0 and number%2==1:
#     print("Positive Odd")
# elif number<0 and number%2==0:
#     print("Negative Even")
# elif number<0 and number%2==1:
#     print("Negative Odd")
# elif number==0:
#     print("Zero")

#question3
# number1=int(input('Enter first'))
# number2=int(input("Enter second"))
# if number1>number2:
#     print("number1 is greater")
# elif number2>number1:
#     print("number2 is greater")
# else:
#     print("Both are equal")

#question4
# number1=int(input('Enter first'))
# number2=int(input('Enter second'))
# number3=int(input('Enter third'))
# if number1<number2 and number1<number3:
#     print("number1 is smallest")
# elif number2<number1 and number2<number:
#     print("number2 is smallest")
# else:
    
#     print("number3 smallest number.")

#question5
# number1=int(input('Enter first'))
# number2=int(input('Enter second'))
# number3=int(input('Enter third'))
# if number1>number2 and number1>number3:
#     print("number1 is largest")
# elif number2>number1 and number2>number:
#     print("number2 is largest")
# else:
    
#     print("number3 largest")


# #question6
# number=int(input("Enter number"))
# if number%5==0 and number%11==0:
#     print("Divisible by both 5 and 11")
# elif number%5==0:
#     print("Divisible only by 5")
# elif number%11==0:
#     print("Divisible only by 11")
# else:
#     print("Divisible by neither")

# #question7
# number=int(input("Enter number"))
# if number%3==0 and number%7==0:
#     print("Divisible by both 3 and 7")
# elif number%3==0:
#     print("Divisible only by 3")
# elif number%7==0:
#     print("Divisible only by 7")
# else:
#     print("Divisible by neither")

# #question8
# marks=int(input("Enter marks"))
# if marks<0:
#     print("Invalid marks")
# elif marks>100:
#     print("Invalid marks")
# elif marks>=40:
#     print("Pass")
# else:
#     print("Fail")

# #question9
# marks=int(input("Enter marks"))
# if marks>=90 and marks<=100:
#     print("a")
# elif marks>=80 and marks>=89:
#     print("b")
# elif marks>=70 and marks>=79:
#     print("c")
# elif marks>=60 and marks>=69:
#     print("d")
# elif marks>=40 and marks>=59:
#     print("e")
# elif marks<40:
#     print("fail")
# if marks<0:
#     print("Invalid marks")
# elif marks>100:
#     print("Invalid marks")

# #question10
# age=int(input("Enter age"))
# if age<0:
#     print("Invalid age")
# elif age<18:
#     print("Cannot vote")
# elif age>18:
#     print("Can vote")

# #question11


# #question14
# Cost_price=int(input("Enter"))
# Selling_price=int(input("Enter "))
# if Selling_price>Cost_price:
#     print("profit")
# elif cost_price>selling_price:
#     print("loss")
# else:
#     print("no profit no loss")

# #question15
# Cost_price=int(input("Enter"))
# Selling_price=int(input("Enter "))
# Profit = Selling_price -Cost_price
# Loss = Cost_price - Selling_price
# profit=Profit/ Cost_price * 100
# loss=Loss / Cost_price * 100
# print(profit)
# print(loss)















# #question17
# First_number=int(input("enter first"))
# Second_number=int(input("enter second"))
# print("+ -*/")
# operator=input("Enter operator")
# if operator=="+":
#     print(First_number +Second_number)
# elif operator=="-":
#     print(First_number -Second_number)
# elif operator=="*":
#     print(First_number*Second_number)
# elif operator=="/":
#     if Second_number!=0:
#         print(First_number/Second_number)


# #question18
# Temperature=int(input("Enter Temperature"))
# if Temperature<0:
#     print("Freezing")
# elif Temperature>0 and Temperature<15:
#     print("very cold")
# elif Temperature>16 and Temperature<25:
#     print("cold")
# elif Temperature>26 and Temperature<35:
#     print("normal")
# elif Temperature>35:
#     print("hot")

# #question19
# number=int(input("Enter number"))
# if number<0:
#     print("negative")
# if number>0 and number<10:
#       print("0-10")
# elif number>11 and number<50:
#      print("11-50")
# elif number>100:
#      print("Above100")
# else:
#      print("")

# #questtion20
# side_one=int(input("Enter sideone"))
# side_Two=int(input("Enter side_two"))
# side_three=int(input("Enter side_three"))
# if side_one+side_Two>side_three:
#     print("Valid triangle")
# elif side_one+side_three>side_Two:
#     print("Valid triangle")
# elif side_Two+side_three>side_one:
#     print("Valid triangle")
#  else:
#      print("inValid triangle")

# #question21
# side_one=int(input("Enter sideone"))
# side_Two=int(input("Enter side_two"))
# side_three=int(input("Enter side_three"))
# if side_one+side_Two>side_three:
#     print("Valid triangle")
# elif side_one+side_three>side_Two:
#     print("Valid triangle")
# elif side_Two+side_three>side_one:
#     print("Valid triangle")
#  else:
#      print("inValid triangle")
# side_one_length=int(input("Enter  side_one_length"))
# side_Two_length=int(input("Enter  side_one_length"))
# side_three_length=int(input("Enter  side_one_length"))
# if side_one_length==side_Two_length==side_three_length:
#     print("Equilateral")
# elif side_one_length==side_Two_length  or side_one_length==side_three_length or side_three_length==side_Two_length:
#     print("Isosceles")
# elif  side_one_length!=side_Two_length  or side_one_length!=side_three_length or side_three_length!=side_Two_length:
#     print("scalene")

# #question22
# Account_balance=float(input("Enter Account balance"))
# withdrawal_Amount=float(input("Enter withdrawalamount"))
# if withdrawal_Amount>0:
#     if  withdrawal_Amount%100==0:
#         if Account_balance>withdrawal_Amount:
#             if Account_balance>500:
#                 print("Withdrawal successful")
#                 Remaining_balance=Account_balance-withdrawal_Amount
#                 print("Remaining balance", Remaining_balance)


# #question23
# username=input("Enter username")
# Password=input("Enter password")
# if username=="admin":
#     if Password=="python123":
#         print("Login successful")
#     else:
#         print("Wrong password")
# else:
    
#     print("User not found")
    
#question24
purchase_amount=int(input("Enter  purchase amount."))
if  purchase_amount<500:
    print("discount percentage","0")
elif purchase_amount>500 and purchase_amount<999:
    print("discount percentage","5")
elif purchase_amount>1000 and purchase_amount<1999:
    print("discount percentage","10")
elif purchase_amount>2000 and purchase_amount<4999:
    print("discount percentage","15")
elif purchase_amount>-5000:
    print("discount percentage","20")















































































































