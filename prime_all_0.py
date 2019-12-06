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

maxNum = 100

primeList = [2]

for i in range(maxNum):
    primeList.append(primeList[i]+1)
    #print(str(primeList[i]))



startTime = time.process_time_ns()
ittrTime = time.process_time_ns()
#print(startTime)
numTest = primeList[0]

for i in primeList:
    lapTime = time.process_time_ns() - ittrTime
    ittrTime = time.process_time_ns()
    numTest = i
    print("prime: " + str(i) + "  in time: " + str(lapTime/1000000) + " mSec")
    # add numbers at the end of the list
    for k in range(i):
        primeList.append(primeList[primeList.__len__()-1] + 1)

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







