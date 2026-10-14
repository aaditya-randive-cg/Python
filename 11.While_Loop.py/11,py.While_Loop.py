#question1
i=1
while i<=5:
    print("Hello")
    i=i+1

#question2
i=0
while i<10:
    print(i,end="")
    i=i+1

#question3
i=1
while i<=10:
    print(i)
    i=i+1

#question4
i = 10
while i >= 1:
    print(i)
    i =i-1

#question5
i = 5
while i <= 50:
    print(i)
    i = i+5

#question6
i = 2
while i <= 20:
    print(i)
    i=i+2

#question7
i = 1
while i <= 19:
    print(i)
    i=i+ 2

#question8
i = 3
while i <= 18:
    print(i)
    i = i+3

#question9
i = 20
while i >= 2:
    print(i)
    i = i-2

#question10
n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i)
    i = i+1

#question11
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
        i =i+ 1

#quest
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i = i+1

#question13
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 3 == 0:
        print(i)
    i =i+ 1

#question14
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 == 0 and i % 3 == 0:
        print(i)
    i =i+ 1

#question15
n = int(input("Enter number2 "))
i = 1
count = 0
while i <= n:
    if i % 2 == 0:
        count += 1
    i = i+1
print(count)

#question16
number = int(input("Enter number"))
sum = 0
i = 1
while i <= number:
    sum = sum + i
    print(sum)

#question17
n = int(input("Enter n: "))
i = 1
sum = 0
while i <= n:
    if i % 2 == 0:
        sum = sum + i
print( sum)

#question18
number=int(input('Enter Number'))
sum=0
i=1
while i<=number:
    if i%2!=0:
        sum=sum+1
    i=i+1
print(sum)
#question19
number=int(input("Enter Number"))
i=1
sum=1
while i<=10:
    sum=i*number
    print(sum)
    i=i+1

#question20
number=int(input("Enter Number"))
i=1
sum=1
while i<=number:
    sum=sum*i
    i=i+1
print(sum)
#question21
word=input("Enter Word")
i=0
while i<=len(word):
    print(word[i])
    i=i+1



















































#question26
i=1
while i<=3:
    j=1
    while j<=4:
        print("*" ,end="")
        j=j+1
    print()
    i=i+1 




'''
number=int(input("enter number"))
while number>0:
    digits=number%10
    print(digits)
    number=number//10


number1=int(input("Enter first number"))
number2=int(input("Enter second number"))
ope=input("Enter operation")
add=number1+number2
sub=number1-number2
mul=number1*number2
div=number1/number2
match ope:
    case 1:
        print(number1+number2)
    case 2:
        print(number1-number2)
    case 3:
        print(number1*number2)
    case 4:
        print(number1/number2)



number1=int(input("Enter Numberone"))
number2=int(input("Enter NUMBERTY"))
ope=input("")
while ope>0:
    if ope=="+":
        print(number1+number2)



    


