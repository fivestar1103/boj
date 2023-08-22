import sys

n, m = map(int, sys.stdin.readline().split())
basketArr = [0] * (n + 1)
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i, j + 1):
        basketArr[idx] = k
for i in range(1, n + 1):
    print(basketArr[i], end=' ')