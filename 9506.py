import sys
from math import sqrt, ceil
def isPerfNum(n):
    tempSum = 0
    tempArr = []
    sqrtN = sqrt(n)
    for i in range(1, ceil(sqrtN)):
        if n % i == 0:
            j = n // i
            if (i == n) or (j==n):
                continue
            tempSum += i + j
            tempArr += [i, j]
            if tempSum > n:
                print("{} is NOT perfect.".format(n))
                return
    
    if sqrtN ** 2 == n:
        tempSum += sqrtN
        tempArr.append(sqrtN)

    if tempSum == n:
        print("{} = ".format(n), end='')
        tempArr.sort()
        for i in range(0, len(tempArr)-1):
            print("{} + ".format(tempArr[i]), end='')
        print(tempArr[-1])
        return
    print("{} is NOT perfect.".format(n))


while True:
    n = int(sys.stdin.readline().rstrip('\n'))
    if n == -1:
        break
    isPerfNum(n)