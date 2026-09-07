#part1 done
#part2 
#question1
text = "Python"

print(text[0])
print(text[3])
print(text[-1])
print(text[-2])


#question2
text = "Programming"

print(text[0:4])
print(text[3:8])
print(text[:5])
print(text[5:])


#ouestion3
text = "Python"

print(text[::2])
print(text[1::2])
print(text[::-1])


#question4
text = "Hello World"

print(len(text))
print(text[5])
print(text[-1])


#question5
text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)


#question6
text = "banana"

print(text.find("a"))
print(text.find("z"))
print(text.count("a"))


#question7
text = "Python"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())


#question8
text = "I like Java"

print(text.replace("Java", "Python"))


#question9
text = "Hello"

print(text + " World")
print(text * 3)


#part3
#question1
name='python'
city='python'
favorite_programming_language='python'


#question2
empty=""
print(empty)
print(len(empty))
print(type(empty))




#question3
name="Python Programming"
print(name[:])
print(len(name))
print(name[0])
print(name[5])
print(name[2])
print(name[4])



#question4
name="Programming"
print(name[0])
print(name[1])
print(name[4])
print(name[-1])

#question5
name="Programming"
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-10])


#question6
name='name'
print(name[0])


#question7
name="Python Programming"
print(name[0:6])
print(name[6:19])
print(name[0:5])
print(name[-1:-5])

#question8
ABCDEFGHIJKL="ABCDEFGHIJKL"
print(ABCDEFGHIJKL[0:12:2])























g="Python Programming"
print(g[-5:])
print(g[-10:])
print(g[::-1])

g="Python Programming"
print(g[:3])
print(g[-3:])
print(g[::2])
print(g[::-1])
# print(g())
first_name="aaditya"
last_name="randive"
print(first_name+last_name)
first_name=" aaditya "
last_name=" randive "
print(first_name+last_name)


name="aaditya"
city="chikhli"
programing_launguage="python"
print(name+city+programing_launguage)

name="aaditya"
b=5
# print(a+b)  type error
print(name+str(b))

a="*"
b=10 
print(a*b)

j="python programming language"
print(j.upper())
print(j.lower())
print(j.capitalize())
print(j.title())
print(j.swapcase())


a="Python"
b="python"
print(a.lower())
print(b.lower())

s="Python is a programming language"
print("Python" in s)
print("programming" in s)
print("Java" in s)
print("language" in s)


s="Python is a programming language"
print(s.find("Python"))
print(s.find("programming"))
print(s.find("Java"))
print(s.find("language"))

s="Python is a programming language"
print(s.find("Java"))
# print(s.index("Java"))


b="banana"
print(b.count("a"))
print(b.count("n"))
print(b.count("b"))


f= "student_notes.pdf"
print(f.startswith("student"))
print(f.endswith(".pdf"))
print(f.endswith(".txt"))

t= "I am learning Java"
print(t.replace("Java","Python."))


d= "apple apple apple"
print(d.replace("apple","mango"))

c= "apple apple apple"
print(c.replace("apple*2","mango*2"))



text = "Python"
print(text.upper())


a="aaditya"
c=a.startswith("aa")
b=a.endswith("ya")
print(c)
print(b)




text = "I like Java"
new_text = text.replace("Java", "Python")
print(new_text)

text = "apple apple apple"
print(text.replace("apple", "mango"))
print(text.replace("apple", "mango", 2))


a="Python"
print("Python" in a)
print("python" in a)
print("python" in a.lower())

#string comparison
a="banana"
b="mango"
print(a==b)

#white spaces
a= "  aaditya  "
print("aaditya" == "  aaditya  ")

#strip
a= "  aaditya  "
print(a.strip())
