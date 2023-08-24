import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))


def check_row(a, x):
    for i in board[a]:
        if i == x:
            return False
    return True


def check_col(b, x):
    for i in range(9):
        if board[i][b] == x:
            return False
    return True


def check_rect(a, b, x):
    na = a // 3 * 3
    nb = b // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[na + i][nb + i] == x:
                return False
    return True


def dfs(i):
    if i == len(blank):
        for i in range(9):
            print(*board[i])
        exit(1)
    for j in range(1, 10):
        x = board[i][0]
        y = board[i][1]
        if check_row(x, j) and check_col(y, j) and check_rect(x, y, j):
            board[x][y] = j
            dfs(i + 1)
            board[x][y] = 0


dfs(0)
