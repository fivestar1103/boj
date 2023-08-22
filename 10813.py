import sys
n, m = map(int, sys.stdin.readline().split())
basketArr = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    basketArr[i], basketArr[j] = basketArr[j], basketArr[i]
for i in range(1, n + 1):
    print(basketArr[i], end=' ')