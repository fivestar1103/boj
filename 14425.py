import sys
n, m = map(int, sys.stdin.readline().rstrip('\n').split())
hashMap = {sys.stdin.readline().rstrip('\n'):None for i in range(n)}
ans = 0
for _ in range(m):
    if sys.stdin.readline().rstrip('\n') in hashMap:
        ans += 1
print(ans)
