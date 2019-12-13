#! python

# from: http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

# Make functions
#def my_split(delimiters, string, maxsplit=0):
#    import re
#    regexPattern = '|'.join(map(re.escape, delimiters))
#    return re.split(regexPattern, string, maxsplit)

import re
import time

print ('Hello, world! ')

searchWin = 10000
maxPrime = 2

primeList = [maxPrime]

for i in range(searchWin):
    primeList.append(primeList[i]+1)
    maxNum = primeList[primeList.__len__() - 1]
    #print(str(primeList[i]))



startTime = time.process_time_ns()
ittrTime = time.process_time_ns()
#print(startTime)

numTest = primeList[0]
for k in primeList:
    for i in primeList:
        numTest = i

        if (maxPrime < i):
            lapTime = time.process_time_ns() - startTime
            #ittrTime = time.process_time_ns()
            maxPrime = i
            print("prime: " + str(maxPrime) + "  in time: " + str(lapTime/1000000) + " mSec  " + "prime percent:" + str(100*primeList.__len__()/maxNum) + "%")
            # add numbers at the end of the list

        for j in primeList:
            if(i < j):
                while (numTest < j):
                    numTest = numTest + i

                if (numTest == j):
                    primeList.remove(j)

    for m in range(searchWin):
        primeList.append(primeList[primeList.__len__()-1] + 1)
        maxNum = primeList[primeList.__len__()-1]


progTime = time.process_time_ns() - startTime
#print(time.process_time())

print(primeList)
print("prine list len:" + str(primeList.__len__()))
print("prime percent:" + str(100*primeList.__len__()/maxNum) + "%")
print("progra time:" + str(progTime/1000000) + " mSec")
#elapsed_time = timeit.timeit(code_to_test, number=100)/100
#print(elapsed_time)







