#Week01_Exercise01_Assignment01
nIterations = 10
MaxVal = float("-inf")
for iterID in range(1,nIterations+1):
    print "Enter number [#%d]: " % iterID
    MaxVal = max(MaxVal, float(raw_input()))
print "Max value is %f" % MaxVal

##### Option B #####
#nIterations = 10
#MaxVal = ""
#for iterID in range(1,nIterations+1):
#    print "Enter number [#%d]: " % iterID
#    if MaxVal == "" :
#        MaxVal = float(raw_input())
#    else :
#        MaxVal = max(MaxVal, float(raw_input()))
#print "Max value is %f" % MaxVal

##### Option A #####
#nIterations = 10
#iterID = 1
#print "Enter number [#%d]: " % iterID
#MaxVal = float(raw_input())
#while iterID < nIterations :
#    iterID += 1
#    print "Enter number [#%d]: " % iterID
#    MaxVal = max(MaxVal, float(raw_input()))
#print "Max value is %f" % MaxVal