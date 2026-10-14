# #question 1
# choice = int(input("Enter your choice: "))

# match choice:
#     case 1:
#         print(" Pizza")
#     case 2:
#         print("Burger")
#     case 3:
#         print(" Pasta")
#     case 4:
#         print("YSandwich")
#     case _:
#         print("Invalide")


# #question2
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Wi-Fi")
#     case 2:
#         print("Bluetooth")
#     case 3:
#         print("Mobile Data ")
#     case 4:
#         print("Airplane Mode ")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Setting")

# #question4
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Check Balance ")
#     case 2:
#         print("Withdraw money ")
#     case 3:
#         print("Deposit money ")
#     case 4:
#         print("Change PIN ")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid choice")

# #question4
# signal = input("Enter signal ")

# match signal:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Wait")
#     case "green":
#         print("Go")
#     case _:
#         print("Invalid Signal")

# #question5
# choice = int(input("Enter category: "))

# match choice:
#     case 1:
#         print("Opening Electronics")
#     case 2:
#         print("Opening Clothing")
#     case 3:
#         print("Opening Books")
#     case 4:
#         print("Opening Grocery")
#     case 5:
#         print("Exit Selected")
#     case _:
#         print("Invalid Category")

# #questiion7
# choice = int(input("Enter service: "))

# match choice:
#     case 1:
#         print("Opening Account Balance")
#     case 2:
#         print("Opening Mini Statement")
#     case 3:
#         print("Opening Fund Transfer")
#     case 4:
#         print("Opening Bill Payment")
#     case 5:
#         print("Opening Customer Support")
#     case _:
#         print("Invalid Service")

# #question8
# choice = int(input("Enter show: "))

# match choice:
#     case 1:
#         print("Morning Show Selected")
#     case 2:
#         print("Afternoon Show Selected")
#     case 3:
#         print("Evening Show Selected")
#     case 4:
#         print("Night Show Selected")
#     case _:
#         print("Invalid Show")

# #question9
# weather = input("Enter weather: ").lower()

# match weather:
#     case "sunny":
#         print("Wear sunglasses")
#     case "rainy":
#         print("Carry an umbrella")
#     case "cloudy":
#         print("Weather may change")
#     case "snowy":
#         print("Wear warm clothes")
#     case _:
#         print("Unknown Weather")

# #question10
# payment = input("Enter payment method: ").lower()

# match payment:
#     case "upi":
#         print("UPI Payment Selected")
#     case "card":
#         print("Card Payment Selected")
#     case "cash":
#         print("Cash Payment Selected")
#     case "wallet":
#         print("Wallet Payment Selected")
#     case _:
#         print("Invalid Payment Method")

# #question11
# extension = input("Enter extension: ").lower()

# match extension:
#     case "pdf":
#         print("Document")
#     case "jpg" | "png":
#         print("Image")
#     case "mp3":
#         print("Audio File")
#     case "mp4":
#         print("Video File")
#     case _:
#         print("Unknown File Type")

# #question12
# role = input("Enter role: ").lower()

# match role:
#     case "admin":
#         print("Full Access")
#     case "teacher":
#         print("Teacher Dashboard")
#     case "student":
#         print("Student Dashboard")
#     case "guest":
#         print("Limited Access")
#     case _:
#         print("Invalid Role")

# #question13
# day = int(input("Enter day number: "))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid Day")

# #question14
# priority = int(input("Enter priority: "))

# match priority:
#     case 1 | 2:
#         print("Normal Priority")
#     case 3 | 4:
#         print("Urgent Priority")
#     case _:
#         print("Invalid Priority")

# #question15
# level = int(input("Enter membership level: "))

# match level:
#     case 1 | 2:
#         print("Basic Membership")
#     case 3 | 4:
#         print("Premium Membership")
#     case _:
#         print("Invalid Membership Level")

# #question16
# user_type = int(input("Enter user type: "))

# match user_type:
#     case 1:
#         print("1. View Courses")
#         print("2. View Marks")
#         print("3. View Attendance")

#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Opening Student Courses")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case _:
#                 print("Invalid Student Option")

#     case 2:
#         print("1. View Students")
#         print("2. Enter Marks")
#         print("3. View Attendance")

#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Opening Teacher Students")
#             case 2:
#                 print("Opening Teacher Marks Entry")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case _:
#                 print("Invalid Teacher Option")

#     case _:
#         print("Invalid User Type")






# # question17

# account = int(input("Enter account type (1-Savings, 2-Current): "))

# match account:
#     case 1:
#         print("Savings Account")
#     case 2:
#         print("Current Account")
#     case _:
#         print("Invalid Account Type")
#         exit()

# operation = int(input("Enter operation (1-Check Balance, 2-Deposit, 3-Withdraw): "))

# match operation:
#     case 1:
#         print("Check Balance Selected")
#     case 2:
#         print("Deposit Selected")
#     case 3:
#         print("Withdraw Selected")
#     case _:
#         print("Invalid Operation")

# #question18
# category = int(input("Enter category (1-Electronics, 2-Clothing): "))

# match category:
#     case 1:
#         product = int(input("Enter product (1-Mobile, 2-Laptop, 3-Headphones): "))
#         match product:
#             case 1:
#                 print("Mobile Selected")
#             case 2:
#                 print("Laptop Selected")
#             case 3:
#                 print("Headphones Selected")
#             case _:
#                 print("Invalid Product")

#     case 2:
#         product = int(input("Enter product (1-Shirt, 2-Jeans, 3-Shoes): "))
#         match product:
#             case 1:
#                 print("Shirt Selected")
#             case 2:
#                 print("Jeans Selected")
#             case 3:
#                 print("Shoes Selected")
#             case _:
#                 print("Invalid Product")

#     case _:
#         print("Invalid Category")

# #question18
# category = int(input("Enter category (1-Electronics, 2-Clothing): "))

# match category:
#     case 1:
#         product = int(input("Enter product (1-Mobile, 2-Laptop, 3-Headphones): "))
#         match product:
#             case 1:
#                 print("Mobile Selected")
#             case 2:
#                 print("Laptop Selected")
#             case 3:
#                 print("Headphones Selected")
#             case _:
#                 print("Invalid Product")

#     case 2:
#         product = int(input("Enter product (1-Shirt, 2-Jeans, 3-Shoes): "))
#         match product:
#             case 1:
#                 print("Shirt Selected")
#             case 2:
#                 print("Jeans Selected")
#             case 3:
#                 print("Shoes Selected")
#             case _:
#                 print("Invalid Product")

#     case _:
#         print("Invalid Category")

# # question19
# category = int(input("Enter category (1-Vegetarian, 2-Non-Vegetarian): "))

# match category:
#     case 1:
#         food = int(input("Enter food (1-Paneer, 2-Dal, 3-Veg Biryani): "))
#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")
#             case 3:
#                 print("Veg Biryani Selected")
#             case _:
#                 print("Invalid Food")

#     case 2:
#         food = int(input("Enter food (1-Chicken Biryani, 2-Chicken Curry, 3-Fish Fry): "))
#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")
#             case _:
#                 print("Invalid Food")

#     case _:
#         print("Invalid Category")


# #question20
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /): ")

# match operator:
#     case "+":
#         print("Result =", a + b)
#     case "-":
#         print("Result =", a - b)
#     case "*":
#         print("Result =", a * b)
#     case "/":
#         if b != 0:
#             print("Result =", a / b)
#         else:
#             print("Cannot divide by zero")
#     case _:
#         print("Invalid Operator")

# #question21
# choice = int(input("Enter choice (1-C to F, 2-F to C): "))
# temperature = float(input("Enter temperature: "))

# match choice:
#     case 1:
#         result = (temperature * 9 / 5) + 32
#         print("Temperature =", result, "F")
#     case 2:
#         result = (temperature - 32) * 5 / 9
#         print("Temperature =", result, "C")
#     case _:
#         print("Invalid choice")



# #question22
# choice = int(input("Enter choice (1-4): "))
# value = float(input("Enter value: "))

# match choice:
#     case 1:
#         print(value * 1000, "meters")
#     case 2:
#         print(value / 1000, "kilometers")
#     case 3:
#         print(value * 1000, "grams")
#     case 4:
#         print(value / 1000, "kilograms")
#     case _:
#         print("Invalid choice")






# #question23
# choice = int(input("Enter choice (1-4): "))
# value = float(input("Enter value: "))

# match choice:
#     case 1:
#         print(value * 1000, "meters")
#     case 2:
#         print(value / 1000, "kilometers")
#     case 3:
#         print(value * 1000, "grams")
#     case 4:
#         print(value / 1000, "kilograms")
#     case _:
#         print("Invalid choice")





# #question24
# choice = int(input("1-Start Exam, 2-View Result, 3-Exit: "))

# match choice:
#     case 1:
#         age = int(input("Enter age: "))
#         if age >= 18:
#             print("You can start the exam")
#         else:
#             print("You cannot start the exam")

#     case 2:
#         print("Opening Result")

#     case 3:
#         print("Exiting Portal")

#     case _:
#         print("Invalid choice")










# #question25
# ticket = int(input("Enter ticket type (1-Regular, 2-Premium, 3-VIP): "))
# age = int(input("Enter age: "))

# match ticket:
#     case 1:
#         if age < 0:
#             print("Invalid Age")
#         elif age < 5:
#             print("Free Entry")
#         else:
#             print("Regular Ticket Selected")

#     case 2:
#         if age < 0:
#             print("Invalid Age")
#         elif age < 5:
#             print("Free Entry")
#         else:
#             print("Premium Ticket Selected")

#     case 3:
#         if age < 0:
#             print("Invalid Age")
#         elif age < 5:
#             print("Free Entry")
#         else:
#             print("VIP Ticket Selected")

#     case _:
#         print("Invalid Ticket Type")
















# #question26
# device = int(input("Enter device (1-Light, 2-Fan, 3-AC, 4-TV): "))

# match device:
#     case 1:
#         print("Light Controller Opened")
#     case 2:
#         print("Fan Controller Opened")
#     case 3:
#         print("AC Controller Opened")
#     case 4:
#         print("TV Controller Opened")
#     case _:
#         print("Invalid Device")
























# #question27
# department = int(input("Enter department (1-5): "))

# match department:
#     case 1:
#         print("General Medicine Selected")
#     case 2:
#         print("Cardiology Selected")
#     case 3:
#         print("Orthopedics Selected")
#     case 4:
#         print("Pediatrics Selected")
#     case 5:
#         print("Emergency Department Selected")
#     case _:
#         print("Invalid Department")




















# #question28
# choice = int(input("Enter choice (1-5): "))

# match choice:
#     case 1:
#         print("Booking Ticket")
#     case 2:
#         print("Cancelling Ticket")
#     case 3:
#         print("Checking PNR")
#     case 4:
#         print("Opening Train Schedule")
#     case 5:
#         print("Exiting Railway System")
#     case _:
#         print("Invalid choice")





# Q29]

# print("1 Search BookIssue Book\n3 Return Book\n4 View Issued Books\n5 Exit")

# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Search Book Selected")
#     case 2:
#         print("Issue Book Selected")
#     case 3:
#         print("Return Book Selected")
#     case 4:
#         print("View Issued Books Selected")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid choice")



# Q30]

# print("placed\nconfirmed\npreparing\nout_for_delivery\ndelivered\ncancelled")

# status = input("Enter status: ").strip().lower()

# match status:
#     case "placed":
#         print("Your order has been placed")
#     case "confirmed":
#         print("Your order has been confirmed")
#     case "preparing":
#         print("Your order is being prepared")
#     case "out_for_delivery":
#         print("Your order is on the way")
#     case "delivered":
#         print("Your order has been delivered")
#     case "cancelled":
#         print("Your order has been cancelled")
#     case _:
#         print("Invalid Order Status")


# Q31]

# print("1 Personal BankingBusiness Banking")

# banking_type = int(input("Enter banking type: "))

# match banking_type:

#     case 1:
#         print("1 BalanceTransfer\n3 Loan")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Personal Banking - Balance Selected")
#             case 2:
#                 print("Personal Banking - Transfer Selected")
#             case 3:
#                 print("Personal Banking - Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 BalancePayroll\n3 Business Loan")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Business Banking - Balance Selected")
#             case 2:
#                 print("Business Banking - Payroll Selected")
#             case 3:
#                 print("Business Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Banking Type")


# 32]

# print("1 StudentTeacher\n3 Parent")

# role = int(input("Enter role: "))

# match role:

#     case 1:
#         print("1 MarksAttendance\n3 Homework")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Student Marks Selected")
#             case 2:
#                 print("Student Attendance Selected")
#             case 3:
#                 print("Student Homework Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 Enter MarksAttendance\n3 Assign Homework")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Enter Marks Selected")
#             case 2:
#                 print("Teacher Attendance Selected")
#             case 3:
#                 print("Assign Homework Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         print("1 Child MarksChild Attendance\n3 Contact Teacher")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Child Marks Selected")
#             case 2:
#                 print("Child Attendance Selected")
#             case 3:
#                 print("Contact Teacher Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Role")



# 33]

# print("1 FlightTrain\n3 Bus")

# transport = int(input("Enter transport: "))

# match transport:

#     case 1:
#         print("1 EconomyBusiness")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Economy Selected")
#             case 2:
#                 print("Business Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 Sleepe AC")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Sleeper Selected")
#             case 2:
#                 print("AC Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         print("1 OrdinaryVolvo")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Ordinary Selected")
#             case 2:
#                 print("Volvo Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Transport")
























'''
for i in range(3):
    print("Python")
else:
    print("Done")

for i in range(1, 5):
    print("A", i)
    if i == 3:
        break
    print("B", i)
'''

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("Value:", i)
#     print("Next line")



