import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))


def check_row(x, a):
    for i in range(9):
        if board[x][i] == a:
            return False
    return True


def check_col(y, a):
    for i in range(9):
        if board[i][y] == a:
            return False
    return True


def check_rect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[nx + i][ny + j] == a:
                return False
    return True


def dfs(i):
    if i == len(blank):
        for j in range(9):
            print(*board[j])
        exit(0)
    for j in range(1, 10):
        x = blank[i][0]
        y = blank[i][1]
        if check_row(x, j) and check_col(y, j) and check_rect(x, y, j):
            board[x][y] = j
            dfs(i + 1)
            board[x][y] = 0


dfs(0)
