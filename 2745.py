import sys
n, b = sys.stdin.readline().rstrip('\n').split()
b = int(b)
n = list(n)
ans = 0
for i in range(len(n)):
    s = n[-(i+1)]
    num = ord(s) - (55 if ord(s) >= 65 else 48)
    ans += b ** i * num
print(ans)