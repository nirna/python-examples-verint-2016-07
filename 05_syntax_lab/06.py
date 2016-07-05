#Week01_Exercise01_Assignment06
from random import randint
x,y,z = randint(1,10),randint(1,10),1
for prime in [2,3,5,7]:
    pwr = 0
    while (x%(prime**(pwr+1))) * (y%(prime**(pwr+1))) == 0 : pwr += 1
    z *= prime**pwr
print "The smallest number devided by [%d] and [%d] is [%d]" % (x,y,z)
