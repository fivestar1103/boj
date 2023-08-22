import sys

n = int(sys.stdin.readline().rstrip('\n'))
myMap = {}
for _ in range(n):
    name, action = sys.stdin.readline().rstrip('\n').split()
    myMap[name] = action
inTheBldg = sorted([i for i in myMap.keys() if myMap[i] == "enter"], reverse=True)
for i in inTheBldg:
    print(i)
