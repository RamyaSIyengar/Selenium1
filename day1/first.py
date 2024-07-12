# this is first python for selenium

print("Hello python for selenium")

x = 100
y = 87

print(x + y)

a = 100
b = 2

print(a ** b)

name = "shraddha"  # %s - string formatting
age = 26  # %d - int
sal = 3.87  # %g - float

print("name is", name, "and age is", age)

# Formatting output - % or {}
print("Name is %s Age is %d sal is %g" % (name, age, sal))
print("Name is {} Age is {} sal is {}".format(name, age, sal))

# taking input from user and formatting

# num1 = int(input("Enter the first number"))
# num2 = int(input("Enter the second number"))
#
# print(type(num1))
# print(num1+num2)
# print("num1: {} num2: {} " .format(num1, num2))

# if num1 % 2 == 0:
#     print("even num {}" .format(num1))
# else:
#     print("odd num {}" .format(num1))

# ternary operator
x = 11
print("even num") if (x % 2 == 0) else print("odd num")

{print("even no"), print(x / 2)} if (x % 2 == 0) else {print("odd num"), print(x / 2)}

# condition statement
week_num = 9

if week_num == 1:
    print("Monday")
elif week_num == 2:
    print("Tuesday")
elif week_num == 3:
    print("wednesday")
elif week_num == 4:
    print("thursday")
elif week_num == 5:
    print("friday")
elif week_num == 6:
    print("saturday")
elif week_num == 7:
    print("sunday")
else:
    print("enter a valid week num")

# Q. print if a num is positive or negative
num = 0

if num > 0:
    print("positive num")
elif num < 0:
    print("negative num")
else:
    print("zero")

# check the largest of two numbers
num1 = 10
num2 = 4578

if num1 > num2:
    print(num1)
else:
    print("largest among num1 and num2 is ", num2)

# check the largest of three numbers
num3 = 890

if num1 > num2:
    if num1 > num3:
        print("num1 is greatest")
    else:
        print("num3 is greatest")
if num2 > num1:
    if num2 > num3:
        print("num2 is greatest")
    else:
        print("num3 is greatest")

# print week no if you give week name

week_name = "wednesday"
print(week_name)
if week_name == "Monday":
    print(1)
elif week_name == "Tuesday":
    print(2)
elif week_name == "wednesday":
    print(3)
elif week_name == "thursday":
    print(4)
elif week_name == "friday":
    print(5)
elif week_name == "saturday":
    print(6)
elif week_name == "sunday":
    print(7)
else:
    print("enter a valid week name")

# range function
print(list(range(-10, 0)))

i = 10
while i > 1:
    print(i)
    i -= 1
print("done")

for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

# ways of writing strings
s1 = "people"
s = str('string')
print(s)

# creating empty string variables

naam = ''
naam1 = str()

# mutable - can change the value of the variable
# immutable - cannot change the value of the variable

# strings are immutable and python will allocate memory to that string variable
# to access the memory address of the string use id

print(id(naam1))

naam1 = naam1 + "python"
print(id(naam1))
# diff memory space created when you try to update the existing string variable
# Mutable objects are those that allow you to change their value or data in place
# without affecting the object's identity. In contrast, immutable objects don't
# allow this kind of operation. You'll just have the option of creating new objects
# of the same type with different value


# diff between + and *

# + concatenation
# * multiple


print(naam1 + " programing")
print(naam1 * 3)

# slicing
print(naam1[1:])
print(naam1[:4])

#ord() and chr()
print(ord('A'))  # 65  ord gives ascii number of character
print(chr(65))  # A ascii code

arr = [34, 56, 21, 56, 90]
print(min(arr))
print(max(arr))

# min() max() len() for strings
print(max("zagf"))
print(min("zagf"))
print(len("zagf"))

# in,  not in operators return true or false

s = "Welcome"
print("elc" in s)
print("Welc" not in s)

# string comparison

print(s == "welcome")
print(s == "Welcome")

# looping statement
# while and for loop

# Print i as long as i is less than 6:
i = 6
while i < 6:
    print(i)
    i += 1

# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("--------")

# A for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).

# 1. using range()- To loop through a set of code a specified number of times
for i in range(1, 11):
    print(i)

for i in range(0, 21, 2):
    print(i)

for i in range(10, -1, -1):
    print(i)

for i in range(5, 101, 5):
    print(i)

# 2 Looping Through a String
name = "Ramya, Iyengar"
for x in name:
    print(x)
print(len(name))

print("am" in name)

if "mya" in name:
    print("present")

# slicing string
print(name[2:])
print(name[-4:-1])

#modify string
print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace('a','e'))
print(name.split(","))

# string concatenation
first_name = "Ramya"
last_name = "Iyengar"
full_name = first_name + last_name
print(full_name)
print(first_name + " " + last_name)

#string format
age = 26
# txt =" my age is " + age # TypeError: must be str, not int
# print(txt)

import random
print(random.randrange(1, 10))

# DATA TYPES IN PYTHON
# List, Tuple, Set, Dictionary

#List
#  Lists are used to store multiple items in a single variable.
#  List items are ordered - If you add new items to a list, the new items will be placed at the end of the list,
#  changeable - we can change, add, and remove items in a list after it has been created.
#  and allow duplicate values -  lists can have items with the same value:.

thisList = ["apple", "banana", "carrot", "apple"]
print(thisList)
print(len(thisList))

# List items can be of any data type:
# lists are defined as objects with the data type 'list'
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# using constructor list()
thisConstructorList = list(("angel", "ballerina", "cupid"))  # note the double rounded bracket
print(thisConstructorList)
print(thisConstructorList[0:2])
if "angel" in thisConstructorList:
    print("yes, apple is in the list")

thisConstructorList[0] = "snowangel"
thisConstructorList[1:2] = ["trinket", "barbie" ]
print(thisConstructorList)
thisList[1:3] = ["watermelon"]
print(thisList)
thisList.insert(2, "muskmelon")
thisList.append("orange")
thisList.extend(thisConstructorList)
thistuple = ("kiwi", "orange")
thisList.extend(thistuple)
print(thisList)

# If there are more than one item with the specified value,
# the remove() method removes the first occurrence:
thisList.remove("apple")
print(thisList)
# The pop() method removes the specified index.
thisList.pop(2)
print(thisList)
# If you do not specify the index, the pop() method removes the last item. pop()


# The del keyword can also delete the list completely.The del keyword also removes the specified index
del thisList[0]
# del thisList

#The clear() method empties the list.

thisList.clear()
print(thisList)


