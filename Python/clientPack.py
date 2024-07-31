import sys

sys.path.append("C:/Users/soundarr/Desktop/python/pythonBasics/pythonProject/Python/pack1")

# pack1 => module1 and module2 and their functions
import module1
import module2

module1.display()
module2.show()

# approach 2
from module1 import *
from module2 import *

display()
show()


# pack2 which is a sub package of pack1 has function exhibit

sys.path.append("C:/Users/soundarr/Desktop/python/pythonBasics/pythonProject/Python/pack1/pack2")
import module3

module3.exhibit()

# getting class method from module1 - pack1

# sys.path.append("C:/Users/soundarr/Desktop/python/pythonBasics/pythonProject/Python/pack1")
# import module1

empObj = module1.Emp(780941, "Ramya", 3.8)
empObj.display_emp()


# Variables in Module

a = module1.person1
print(a)

#Built-in Modules

import platform

x = platform.system()
y = platform.machine()
z = platform.python_version()
print(x, y, z)

# The dir() function can be used on all modules, also the ones you create yourself.
listAllFun = dir(platform)
print(listAllFun)