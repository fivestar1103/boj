import sys
n = int(sys.stdin.readline().rstrip('\n'))
arr = [None, 3]
for i in range(n-1):
    top = arr[-1]
    arr.append(top * 2 -1)
print(arr[n]**2)