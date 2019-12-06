#! python

# from: http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

# Make functions
#def my_split(delimiters, string, maxsplit=0):
#    import re
#    regexPattern = '|'.join(map(re.escape, delimiters))
#    return re.split(regexPattern, string, maxsplit)

import re

print ('Hello, world!')

class Anumber:
    #value = 0
    #next_number = 0
    def __init__(self, x=0):
        self.value = x
        self.nextNumber = None

    def SetNext(self,num):
        self.nextNumber = num

    def GetNext(self):
        return self.nextNumber

    def GetValue(self):
        return self.value


### END Class ====================================




NumberListHead = Anumber(2)

NumberListCurrent = NumberListHead
print (str(NumberListCurrent.GetValue() ))

for i in range(1000):
    NumberListCurrent1 = Anumber(NumberListCurrent.GetValue()+1)
    NumberListCurrent.SetNext(NumberListCurrent1)
    NumberListCurrent = NumberListCurrent1
    print (str(NumberListCurrent.GetValue() ))

numberCheck = NumberListHead.GetValue()
numberCheckAdd = numberCheck

currentScan = NumberListHead
nextScan = currentScan.GetNext()


while(currentScan.GetNext() != None):

    numberCheckAdd = numberCheckAdd+numberCheck

    if (numberCheckAdd > nextScan.GetValue()):

        currentScan
    else:
        if (numberCheckAdd == nextScan.GetValue())
            currentScan = nextScan.G





