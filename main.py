'''
Exercise 3b

Explore the Decimal class (http://mng.bz/oPVr), which has an alternative
floating-point representation that is as accurate as any decimal number can be.
Write a function that takes two strings from the user, turns them into decimal
instances, and then prints the floating-point sum of the users two inputs. In
other words, make it possible for the user to enter 0.1 and 0.2 , and for us to get
0.3 back.

'''
from decimal import *
# The decimal class takes strings as arguements.

def sum(num1, num2):
    dec1 = Decimal(str(num1)) 
    dec2 = Decimal(str(num2))
    return dec1 + dec2

print(sum(15.1119, 25.2858))
print(sum(0.1, 0.2)) 