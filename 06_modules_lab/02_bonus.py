""" 
Print sum of two input  + check inputs
"""
#Week01_Exercise02_Assignment02_Bonus
import sys
if len(sys.argv) != 3: print 'Syntax Error. Syntax is:\npython %s <integer_value_1> <integer_value_2>' % sys.argv[0]
else:
    try:
        x,y = int(sys.argv[1]),int(sys.argv[2])
        print 'Sum of %d and %d is %d' %(x,y,x+y)
    except ValueError:
        print 'Syntax Error. Syntax is:\npython %s <integer_value_1> <integer_value_2>' % sys.argv[0]
