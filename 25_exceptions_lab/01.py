"""
Write a python program that takes numbers in a loop
and for each number prints its square root
If value is negative or not a number show 
a warning and keep reading values
"""
import math

while True:
    try:
        n = float(raw_input("Enter a nmber: "))
        print "The square root of %f is %f" %(n,math.sqrt(n))

    except ValueError as e:
        print "Failed to calculate square root. Error was: %s" % e.message
