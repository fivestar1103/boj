import sys
n = int(sys.stdin.readline().rstrip('\n'))
fiboArr = [1] * (n + 1)
for i in range(3, n+1):
    fiboArr[i] = fiboArr[i-1]+fiboArr[i-2]
print(fiboArr[n], n-2)
