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