""" return a dictionary of keys (func outputs) and list of values """

from collections import defaultdict

def groupby(myfunc, *mylist):
    mydict = defaultdict(list)
    for item in mylist: mydict[myfunc(item)].append(item)
    return mydict

# returns: { h: [�hello�, �hi�, �help�, �here�], b: [�bye�] }
print groupby(lambda(s): s[0], 'hello', 'hi', 'help', 'bye', 'here')