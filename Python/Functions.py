
"""

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""


# # *args = Arbitrary arguments
# def my_func(*name):
#     print("hi", name[2])
#
#
# my_func("Rashmi", "Ramya", "Ashwin")
#
#
# # *kwargs = keyword arguments
# def this_func(child2, child3, child1):
#     print("the second child",child2)
#
#
# this_func(child1="Rashmi", child2="Ramya", child3="Ashwin")


# recursion

def recursion(k):
    if k > 0:
        result = k + recursion(k-1)
        print(result)
    else:
        result = 0
    return result


recursion(2)


two = lambda x: x*10

print(two(10))


def myfunc(n):
    return lambda a: a*n+1


doubler = myfunc(2)
print(doubler(100))


