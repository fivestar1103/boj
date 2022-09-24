import sys
s = [None] + list(sys.stdin.readline().rstrip('\n'))
lenS = len(s) - 1
hashMap = {}
for length in range(1, lenS + 1):
    for start in range(1, lenS + 2 - length):
        tmp = ''.join(s[start:start+length])
        if tmp not in hashMap:
            hashMap[tmp] = None
print(len(hashMap))
