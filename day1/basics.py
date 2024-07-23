import keyword

print(keyword.kwlist)  # prints all available keyword
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']
'''

# DataTypes

print(dir(keyword))  # all variables and function names

# ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
# 'iskeyword', 'issoftkeyword', 'kwlist', 'softkwlist']

# delete the variable
'''
a = 100
del a
print(a)
'''

# Variables

'''
a=b=c=100
a,b,c=10,20,'welcome'

x=1
y=2
print(x,y)  #1 2
y,x=x,y
print(x,y)  #2 1

'''


# operators


result1 = -17 // 5
print("Floor division of two integers :", result1)

# -17 / 5 = -3.4
# -17 / -5 = 3.4
# -17 // 5 = -4
# -17 // -5 = 3

# concatenation
# True = 1   False = 0
print(True + 5)  # 6
print(False * 3)  # 0
# print("welcome" + 5)  #TypeError: can only concatenate str (not "int") to str

# print(True + "welcome")  # TypeError: unsupported operand type(s) for +: 'bool' and 'str'


# format

name = "Ramya"
age = 26
sal = 33.00

print("name is : %s age is: %d sal is %g" % (name, age, sal))
print("name is: {} age is: {} sal is {}" .format(name, age, sal))


# taking input

'''
num1 = input('Enter a num')  # 1
num2 = input('Enter a num')  # 2
print(num1+num2)  # 12

num1 = int(input('Enter a num'))  # 3
num2 = int(input('Enter a num'))  # 4
print(num1+num2)  # 7
'''
# conditional statement if if elif else

# Largest of 2 numbers
a, b = 10, 20
print("a is largest") if a > b else print("b is largest")

# Largest of 3 numbers
a, b, c = 10, 20, 30
if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")

# ternary operator with if else
num = 11
# print("Even num") if num % 2 == 0 else print("odd num")
# {print("odd num"), print(num)} if num <= 10 else {print("Even num"), print(num)}

# range
# print(list(range(10)))
# print(list(range(0, 10, 2)))

# Looping statements - while and for
i = 1
while i <= 10:
    print(i)
    i += 1


i = 10
while i >= 1:
    print(i)
    i -= 1

# for

# for i in "apple":
#     print(i)
#
# for i in ["pop", "ser", "hut"]:
#     print(i)
#
# for i in range(1, 10):
#     print(i*90)
for i in range(1, 11):
    if i == 9 or i == 5 or i == 3:
        continue
    print(i)

for i in range(2, 20, 2):
    if i == 14:
        break
    print(i)

# for i in range(10, 0, -1):
#     print(i)
#
# for i in range(0, 101, 5):
#     print(i)

# max and min of nums

print(max(10, 20, 30))
print(min(10, 20, 30))


# strings
fname = ''  # creating empty string variable
lname = str()

# mutable - can change the value of the variable
# immutable - cannot change the value of the variable

# strings are immutable - can't be changed
str1 = "welcome"
print(id(str1))  # 1552723646064

str1 = str1 + "back"
print(id(str1))  # 1552723646320

print(str1[1:-1])  # elcomebac
print(str1[1:-3])  # elcomeb


# ord() and chr()
print(ord('A'))  # 65
print(ord('a'))  # 97
print(chr(100))  # d

# min max len => str

print(max("ABZ"))  # Z
print(min("ABZ"))  # A
print(len("ramya"))

str1 = "welcome"
if "come" in str1:
    print("yes")

# in and not in operators returns true or false
print("come" in str1)  # True
print("come" not in str1)  # False

# testing strings true or false
print(str1.isalnum())  # True  Return True if the string is an alpha-numeric string
print("welcome".isalpha())  # True
print("2024".isdigit())  # True
print("True of".isidentifier())  # False
print("abc".islower())
print("abc".isupper())
print(" ".isspace())

# Search for subStrings

s = "welcome to Python"

print(s.endswith("on"))  # True
print(s.startswith("foo"))  # False
print(s.find("Python"))  # 11
print(s.find("java"))  # -1  not found
print(s.count("o"))  # 3  occurrence of the substring


s1 = s.capitalize()
print(s1)  # Welcome to python

s2 = s.title()
print(s2)

s5 = s.swapcase()
print(s5)  # sTRING IN python

s6 = s.replace("me", "you")
print(s6) # String on PYTHON

# Example12: Reverse a stringMethod1
s = "welcome"
rev_str = ""
for i in s:
    print(i)
    rev_str = i + rev_str # emoclew
print("reversed string is:", rev_str)


reverse_str = s[::-1]
print(reverse_str)
