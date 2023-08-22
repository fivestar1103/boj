import sys
n, m = map(int, sys.stdin.readline().split())
basketArr = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    basketArr[i:j+1] = reversed(basketArr[i:j+1])
'''    length = j - i + 1
    count = length // 2
    for k in range(count):
        basketArr[i+k], basketArr[j-k] = basketArr[j-k], basketArr[i+k]
'''
for i in range(1, n + 1):
    print(basketArr[i], end=' ')