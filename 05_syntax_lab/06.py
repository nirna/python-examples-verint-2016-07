"""
Write a program that randomizes 2 numbers
and calculates their least common multiplier,
that is the smallest number that is divisable
by both.
For example if the numbers were 4 and 6,
program should print 12
"""
#Week01_Exercise01_Assignment06
from random import randint
from fractions import gcd
x,y = randint(1,10),randint(1,10)
print "The smallest number devided by [%d] and [%d] is [%d]" % (x,y,x*y/gcd(x,y))



