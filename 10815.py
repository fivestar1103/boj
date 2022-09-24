import sys
n = int(sys.stdin.readline().rstrip('\n'))
hashMap = {i:None for i in list(map(int, sys.stdin.readline().rstrip('\n').split()))}
m = int(sys.stdin.readline().rstrip('\n'))
scan = list(map(int, sys.stdin.readline().rstrip('\n').split()))
for i in scan:
    print(1 if i in hashMap else 0, end=' ')