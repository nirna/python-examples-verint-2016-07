""" func1: sum all inputs; func2: multiply all inputs """
import numbers

def mysum(*nums):
    return sum([n for n in nums if isinstance(n, numbers.Number)])

def mymul(*nums):
    mul = 1
    for n in nums:
        if isinstance(n, numbers.Number): mul *= n
    return mul

# returns 60
print mysum(10, 20, 30)

# returns 30
print mysum(10, 'foo', 'bar', 20)

# returns 1
print mymul()

# returns 200
print mymul('foo', 'bar', 10, 20)