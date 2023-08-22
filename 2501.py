import sys
n, m = map(int, sys.stdin.readline().rstrip('\n').split())
for i in range(1, n + 1):
    if n % i == 0:
        m -= 1
        if m == 0:
            print(i)
            sys.exit()
print(0)