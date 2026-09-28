#question1
'''string=int(input("Enter string"))
'''


'''
#question2
fail=0
Pass=0
good=0
Excellent=0
for i in range(1,11):
    mark=int(input("Enter marks of student"))
for j in range(1,11):
    if mark<35:
        fail=fail+1
        print("Fail")
    elif mark>=35 and mark<=49:
        Pass=Pass+1
        print( "Pass")
    elif mark>=50 and mark<=74:
        good=good+1
        print("Good")
    elif mark>=75 and mark<=100:
        Excellent=Excellent+1
        print("Excellent")
    print(fail,"Fail")
    print(Pass,"pass")
    print(good,"good")
    print(Excellent,"Excellect")  
        


#question3
const=0
vovel=0
digits=0
special=0
sentence=input("Enter sentence")
for i in sentence:
    if sentence=="A"or"E"or"I"or"O"or"U"or"a"or"e"or"i"or"o"or"u":
        vovel=vovel+1
    elif chr(65)<= i <=chr(90) or chr(97)<= i <=chr(122):
        const=const+1
    elif chr(48)<= i <=chr(57):
        digits=digits+1
    elif chr(32)<= i <=chr(126):
        special=special+1
if const>vovel and const>digits and const>special:
    print(const,"const")
elif vovel>const and vovel>digits and vovel>special:
    print(vovel,"vovel")
elif digits>const and digits>vovel and digits>special:
    print(digits,"digits")
elif special>const and special>vovel and special>digits:
    print(special,"special")


#question4
for j in range(1,6):
    is_length=False
    is_upper=False
    is_lower=False
    is_digit=False
    is_special=False
    password=input("Enter password")
    if len(password)>=8:

        is_length=True
    for i in password:
        if chr(65)>= i <=chr(90):
            is_upper=True
        elif chr(97)>=i <=chr(122):
            is_lower=True
        elif chr(48)>= i <=chr(57):
            is_digit=False
        else:
            is_special=True
        count_length=int(is_length)
        count_upper=int(is_upper)
        count_lower=int(is_lower)
        count_digit=int(is_digit)
        count_special=int(is_special)
        count=count_length+count_upper+count_lower+count_digit+count_special
        if count==5:
            print("strong")
        elif count>=3 and count>=4:
            print("medium")
        else:
            print("weak")
#question5
sentence=input("Enter sentence")
for 

#question8
for i in range(9):
    price=float(input("Enter Price"))
    budget=0
    regular=0
    premium=0
    luxury=0
    if price<500:
        print("budget")
        budget=budget+1
    elif price>=500 and price<=1999:
        print("regular")
        regular=regular+1
    elif price>=2000 and price<=4999:
        print("premium")
        premium=premium+1
    elif price>=5000:
        print("Luxury") 
        luxury=luxury+1
total=budget+regular+premium+luxury
print(total)
print("buget",budget)
print("regular",regular)
print("premium",premium)
print("luxury",luxury)

#question5
count=0
sentence=input("Enter sentence")
for i in sentence:
    count=count+1
length=count
print(length)
if length<=3:
    print("short")
elif length>4 and length<6:
    print("medium")
elif length>6:
    print("long")
  

#question6
for i in range(1,6):
    number=int(input("Enter Number"))
    convert_string=str(number)
    for i in number:
        print(number)
   
        

#question7
string=input("Enter string")
for i in string:
    if i      

#question9
string=input("Enter string")
for i in string:
    print(i)
for r in range(1,6):
    for c in range(i):
        if c==i or c==5 
     '''
