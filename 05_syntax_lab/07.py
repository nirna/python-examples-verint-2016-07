#Week01_Exercise01_Assignment07
from random import randint
pcSelection = randint(1,100)
while True:
    print "Enter your guess (integer):"
    usrSelection = int(raw_input())
    if randint(1,100) < 90 : # do not introduce error
        if usrSelection < pcSelection: print "Too small..."
        elif usrSelection > pcSelection: print "Too big..."
        else: break
    else : # introduce error
        if usrSelection < pcSelection: print "Too big..."
        else: print "Too small..."
print "Yeeaaaaaaaa!!!"
