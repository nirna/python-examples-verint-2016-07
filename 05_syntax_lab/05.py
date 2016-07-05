#Week01_Exercise01_Assignment05
from random import randint
x = randint(1,1000000)
while (x%7)+(x%13)+(x%15) : x = randint(1,1000000) # Since GCD of 7, 13, 15 is 1 you can also use x % (7 * 13 * 15)
print "Found the number %d (%d/%d=%d; %d/%d=%d; %d/%d=%d)" % (x,x,7,x/7,x,13,x/13,x,15,x/15)