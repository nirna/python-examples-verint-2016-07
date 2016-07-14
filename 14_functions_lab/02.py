""" Throw exception if argument 1 s not a number or argument 2 is not string """
import numbers

def myfunc(myint,mystr):
    if not isinstance(myint, numbers.Number): raise Exception("No numeric value")
    if type(mystr) != str: raise Exception("No string value")