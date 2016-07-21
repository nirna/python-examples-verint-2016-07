""" Class MyCounter: counts the numer of objects instances generated """

class MyCounter(object):
    count = 0

    def __init__(self):
        MyCounter.count += 1


#### MAIN ####

for _ in range(10):
     c1 = MyCounter()

# should print 10
print MyCounter.count