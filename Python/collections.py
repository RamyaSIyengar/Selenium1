#List

# list1 = [1,2,3,4]
# print(list1)
# print(list1[2])
# print(list1[-1])
#
# print(list1[1:4])
# print(list1[-4:-1])
#
# list1[3] = 5
# print(list1)
# list1[2:3] = [5,67,89]
# print(list1)
#
# for i in list1:
#     print(i)
#
# if 89 in list1:
#     print("yes")
#
# if 2 not in list1:
#     print("2 is not present")
# else:
#     print("2 is present")
#
# print(len(list1))
# print(type(list1))
#
# # add items to list => append, insert
#
# thislist = ['apple', 'banana', 'cherry']
#
# thislist.append('orange')  # added at last
# print(thislist)
#
# thislist.insert(1, "mango")  # added at specific index
# print(thislist)
#
# # remove items from list
#
# x = thislist.pop(0)  # remove from specific index
# print(thislist)
# print("removed item from list:", x)
#
# del thislist[1]  # delete specific index item
# # del list1
# # print(list1)  # throws err as list1 is no longer exist
#
# thislist.remove('cherry')
# print(thislist)
#
# # copying list
#
# list2 = thislist
# print(list2)
#
# list3 = list(thislist)
# print(list3)
#
# # extend list
#
# thislist.extend(list1)
# print(thislist)

# looping

# for i in thislist:
#     print(i)

# for i in range(len(thislist)):
#     print(thislist[i])  # using indexes

# [print(i) for i in thislist]   # using list comprehension
#
# # join lists
# joinLists = list1 + thislist
# print(joinLists)
# for i in list1:
#     thislist.append(i)
# list1.extend(list2)

# List comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "e" in x]
# print(newlist)


# tuple

