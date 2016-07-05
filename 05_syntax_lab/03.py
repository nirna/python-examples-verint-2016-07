#Week01_Exercise01_Assignment03
from random import randint
SumDigits = 0
x = "%d" % randint(1,10000)
for k in range(0,len(x)) : SumDigits += int(x[k])
print "The sum of digits of %s is %d" % (x, SumDigits)