#! python

# from: http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

# Make functions
#def my_split(delimiters, string, maxsplit=0):
#    import re
#    regexPattern = '|'.join(map(re.escape, delimiters))
#    return re.split(regexPattern, string, maxsplit)

import re
import time

print ('Hello, world!')

maxNum = 100000

primeList = [2]

for i in range(maxNum):
    primeList.append(primeList[i]+1)
    #print(str(primeList[i]))

startTime = time.process_time_ns()
#print(startTime)
numTest = primeList[0]

for i in primeList:
    numTest = i
    for j in primeList:
        if(i < j):
            while (numTest < j):
                numTest = numTest + i

            if (numTest == j):
                primeList.remove(j)

progTime = time.process_time_ns() - startTime
#print(time.process_time())

print(primeList)
print("prine list len:" + str(primeList.__len__()))
print("prime percent:" + str(100*primeList.__len__()/maxNum) + "%")
print("progra time:" + str(progTime/1000000) + " mSec")
#elapsed_time = timeit.timeit(code_to_test, number=100)/100
#print(elapsed_time)







