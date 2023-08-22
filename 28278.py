import sys
def func(myList):
    global myStack
    cmd = myList[0]
    lenStack = len(myStack)
    if cmd == 1:
        num = myList[1]
        myStack.append(num)
    elif cmd == 2:
        print(myStack.pop() if lenStack else -1)
    elif cmd == 3:
        print(lenStack)
    elif cmd == 4:
        print(0 if lenStack else 1)
    else:
        print(myStack[-1] if lenStack else -1)    


n = int(sys.stdin.readline().rstrip('\n'))
myStack = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    func(temp)
