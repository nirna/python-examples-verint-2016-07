"""
Write a program that reads lines from the user
until an empty line is inserted.
After the user typed in an empty line,
print all previously inserted lines in reverse
order (from last to first)
"""
#Week01_Exercise01_Assignment04
TextOut = ""
print "Enter first line (press enter to quit): "
TextIn = raw_input()
while len(TextIn) : 
    TextOut = (TextIn + "\n" + TextOut)
    print "Enter next line (press enter to quit): "
    TextIn = raw_input()
print "Input rows in reverse order:\b%s" % TextOut