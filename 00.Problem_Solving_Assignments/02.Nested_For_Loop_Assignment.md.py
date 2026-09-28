'''
#question1
for r in range(1,4):
    for c in range(1,4):
        print("*",end=" ")
    print()

#question2
for i in range(1,4):
    for j in range(1,4):
        print(j,end="")
    print()

#question3
for i in range(1,4):
    for j in range(1,4):
        print(i,end="")
    print()
#question4
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print("*", end=" ")
    print()

#question5
for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print("*",end=" ")
    print()

#question6
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print(j, end="")
    print()


#question7
for i  in range(1,6):
    for j in range(1,6):
        if i>=j:
            print(i,end="")
    print()


#question10
for i in range(1,6):
    for j in range(1,6):
        print(j*j,end="")
    print()      

#question11
for i in range(1,6):
    for j in range(1,6):
        print(chr(65+j-1),end="")
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()


#question13
for i in range(1,6):
    for j in range(1,6):
        if j%2!=0 :
            print(j ,end="")
    print()

for i in range(1,6):
    a=1
    for j in range(i):
        print(a,end="")
        a+=2
    print()

for i in range(1,6):
    for j in range(1,2*i,2):
        print(j,end="")
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j-1,end="")
    print()
#question15
for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()

#question16
for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print()

#question17
for i in range(1,4):
    for j in range(1,3):
        print()
#question19
for i in range(1,4):
    for j in range(1,4):
        print(f"({i},{j})", end="")
    print()

#question20
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

#question21
for i in range(1,11):
    for j in range(1,11):


#question22
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print(i ,end="")
    print()

#question23
for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print(j,end="")
    print()

#question24
for i in range(1,6):
    for j in range(5,i,-1):
        print(j,end="")
    print()

#question25
for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print()

i=2
while i<=20:
    print(i)
    i=i+2
for i in range(1,11):
    print(i*5)

year=int(input())
if year%100==0 and year%400==0:
    print("leap")
elif year%100!=0 and year%4==0:
    print("leap")
else:
    print("le")

number=int(input("number"))
for i in range(1,11):
    print(f'{number}x{i}={number*i}')
even=0
odd=0
even=0
odd=0
number=int(input("numbers"))
for i in range(1,number+1):
    if i%2==0:
        even=even+1
    elif i%2!=0:
        odd=odd+1
print(even,"even")
print(odd,"odd")
number=int(input("number"))
for i in range(1,number+1):
    if number%i==0:
        print(i)
number=int(input("number"))
sum=0
for i in range(1,number+1):
    if i%number==0:
        continue==number
        sum=sum+i
print(sum)

s=0
number=int(input("number"))
for i in range(1,number):
    if number%i==0:
        s=s+1
if s==2:
    print("prime")
'''

string=input("enter")
for i in range(len(string)):
    