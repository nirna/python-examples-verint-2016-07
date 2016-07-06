"""
Write a program that randomizes a number
and prints the sum total of its digits.
For example if the number was: 2345
The result should be: 14
"""
#Week01_Exercise01_Assignment03
from random import randint
sum_digits = 0
x = "%d" % randint(1,10000)
for digit in x : sum_digits += int(digit)
print "The sum of digits of %s is %d" % (x, sum_digits)