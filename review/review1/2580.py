import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))


def check_row(x, a):
    for i in board[x]:
        if i == a:
            return False
    return True


def check_col(y, a):
    for i in range(9):
        if board[i][y] == a:
            return False
    return True


def check_rect(x, y, a):
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[x + i][y + i] == a:
                return False
    return True


def recursive(idx):
    if idx == len(blank):
        for i in range(9):
            print(*board[i])
        exit(0)
    for i in range(1, 10):
        x, y = blank[idx][0], blank[idx][1]
        if check_row(x, i) and check_col(y, i) and check_rect(x, y, i):
            board[x][y] = i
            recursive(idx + 1)
            board[x][y] = 0


recursive(0)
