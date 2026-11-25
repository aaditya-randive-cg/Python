# #1
# def city():
#     city="city"
#     print(city)

# #2
# school="sigv"
# def fun():
#     print(school)

# #3
# if True:
#     city="navsari"
# print(city)

# #4
# for i in range(10):
#     count=1
# print(i)

#5
#scop means a veriable till we can access
#variablelifetime means how long variable exist


#6
#200
#100

# #7
# clicks = 1
# def click():
#     global clicks
#     clicks = clicks + 1
# click()
# print(clicks)

# #8
# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()cannot access local variable 'name' where it is not associated with a value

# #9
# def outer():
#     o="o"
#     def inner():
#         print(o)
#     return inner

# #10
# def list_funn():
#     a=["1","2","3","4"]
#     return a
# print(list_funn())

# #11
# def outer():
#     count = 0

#     def inner():
#         nonlocal count
#         count += 1
#         return count

#     return inner

# counter = outer()

# print(counter())  # 1
# print(counter())  # 2
# print(counter())  # 3

# #12
# 3
# 2
# 1

#13


# #14
# def outer():
#     message = "Hello Python"

#     def inner():
#         print(message)

#     return inner


# result = outer()
# result()

#15
#it's already a keyword

