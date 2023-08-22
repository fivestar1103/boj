import sys
board = [None]
for _ in range(5):
    word = list(sys.stdin.readline().rstrip('\n'))
    tmp = [None] + word + [None] * (15 - len(word))
    board.append(tmp)
for col in range(1, 16):
    for row in range(1, 6):
        if board[row][col] != None:
            print(board[row][col], end='')