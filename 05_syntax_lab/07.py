""" 
Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a while
"""
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
        print "Too big..." if usrSelection < pcSelection else "Too small..."
print "Yeeaaaaaaaa!!!"
