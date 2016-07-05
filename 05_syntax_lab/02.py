#Week01_Exercise01_Assignment02
from random import randint
nIterations = 7
Sum7 = 0
for iterID in range(0,nIterations) : Sum7 += randint(1,100)
print "The sum of the %d random integers is: %d%s" % (nIterations, Sum7, " - Boom!!!" if Sum7 % 7 == 0 else "")