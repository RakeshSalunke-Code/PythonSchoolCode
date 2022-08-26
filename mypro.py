

#a = 30
#b = "Rakesh"
#c = 10.21

#print(a + 9)

#variable should start with a letter or an underscore
#variable cannot start with a number
#it can only contain alpha numeric charector
#variable names are case sensetive. Harry and harry are different variables.

#typeA = a
#print(type(a))
 
#e = "31"
#e = int(e)
#e = float(e)
#e = str(e)
#print(type(e))
#print(e +2 ) ...  


#x = "20"
#x = int(x)
#x = float(x)
#print(type(x))
#print(x + 2)


#y = "Rakesh"
#z = 20


# STRING

# name = "Rakesh"
# print(name)

#name = Rakesh
           #is a good boy
#print(name)

#print(name)

# Slicing
# name = "Rahul"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print("\n")
# print(name[1:3])
# print(name[1:4])
# print(name[1:5])

# Remove Spacing and length, upper, lower, replace

# name = "Rakesh,Salunke"
# print(name.strip())
# var = name.lower()
# var = name.upper()
# var = name.replace(",","\n")
# print(var)

# # Dot Format
# name1 = "Rakesh"
# name2 = "Mrunali"

# # temp = "My name is {1} and my sister name is {0}".format(name1, name2)
# temp = f"My name is {name1} and my sister name is {name2}"
# print(temp)


# operators
# 1. ** Exponential operators
# 2. // floor division operators
# 3. + - * / 
# 4. % modulo operators

'''
Python Collections
1. List
2. Tuple
3. Set
4. Dictionary
'''
# 1. List
# lst = {61,2,3,4,5,41}
# var = type(lst)
# var = lst[1:4]
# lst.append(100)
# lst.insert(3,100)
# lst.remove(61)
# lst.pop()
# # del lst(3)
# lst.clear()
# print(var)

# 2.Tuple
# a =("Harry","Rakesh","Shubh","Rahul")
# var = a
# var = type(a)
# # a[0] = "Vikrant"   You cannot do this
# print(var)

# # 3. Set

# s1 = {2,3,4,5,6,2,4,5,2,1,11,2,3,4,8}
# s1.add(29)

# print(s1)

# 4. Dictionary

# rakeshDict = {
#     "Name": "rakeshDict",
#     "Class": "10th",
#     "Marks": 250,
#     "HIC": 6
# }   
# print(rakeshDict)

# User Input

# age = input("Enter Your Age\n")
# age = int(age)

# if(age>18):
#     print("You can drive a car")
# else:
#     print("Access Denied")
# print(age)


#Loops

# for i in range(0, 1000):
#     print(i)
# print("Its Done")
# i = 1
# while(i<100)
#   print(i)
#   if i == 78:
#       break
# print(i)

# def greet():
#     print("Good Morning sir")

# greet()

def sum(a,b):
    c = a + b
    return c
d = sum( 34, 34)
print(d)