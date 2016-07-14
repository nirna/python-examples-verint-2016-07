""" sum the 10^1 digits of all input numbers """

import numbers

def sum10(*nums):
    return sum([(n / 10) % 10 for n in nums if isinstance(n, numbers.Number)])

print sum10(140,220,1120)