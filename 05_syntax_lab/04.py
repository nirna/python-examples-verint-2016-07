#Week01_Exercise01_Assignment04
TextOut = ""
print "Enter first line (press enter to quit): "
TextIn = raw_input()
while len(TextIn) : 
    TextOut = (TextIn + "\n" + TextOut)
    print "Enter next line (press enter to quit): "
    TextIn = raw_input()
print "Inout rows in reverse order:\n\n%s" % TextOut
