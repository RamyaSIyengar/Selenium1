import datetime

x = datetime.datetime.now()
print(x)  # 2024-07-31 20:28:43.565571
# The date contains year, month, day, hour, minute, second, and microsecond.

print(x.year)  # 2024
print(x.strftime("%A")) # Wednesday

# Creating Date Objects
"""
To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.
"""

createDate = datetime.datetime(2024, 7, 31)
print(createDate)

# The strftime() Method

"""
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
"""

import datetime

strFormat = datetime.datetime(2024, 7, 31)

print(strFormat.strftime("%B"))  # July
print(strFormat.strftime("%d"))  # 31
print(strFormat.strftime("%A"))  # 00


