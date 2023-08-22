import sys
n, b = map(int, sys.stdin.readline().rstrip('\n').split())
ans = []
while True:
    temp = n%b
    if temp > 9:
        temp = chr(temp+55)
    ans.append(temp)
    n //= b
    if n == 0:
        break
for i in reversed(ans):
    print(i, end='')