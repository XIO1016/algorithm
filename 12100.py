import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def up(board):
    for j in range(n):
        ptr = 0
        for i in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[ptr][j] == 0:
                    board[ptr][j] = tmp
                elif board[ptr][j] == tmp:
                    board[ptr][j] *= 2
                    ptr += 1
                else:
                    ptr += 1
                    board[ptr][j] = tmp
    return board


def down(board):
    for j in range(n):
        ptr = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[ptr][j] == 0:
                    board[ptr][j] = tmp
                elif board[ptr][j] == tmp:
                    board[ptr][j] *= 2
                    ptr -= 1
                else:
                    ptr -= 1
                    board[ptr][j] = tmp
    return board


def left(board):
    for i in range(n):
        ptr = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][ptr] == 0:
                    board[i][ptr] = tmp
                elif board[i][ptr] == tmp:
                    board[i][ptr] *= 2
                    ptr += 1
                else:
                    ptr += 1
                    board[i][ptr] = tmp
    return board


def right(board):
    for i in range(n):
        ptr = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][ptr] == 0:
                    board[i][ptr] = tmp
                elif board[i][ptr] == tmp:
                    board[i][ptr] *= 2
                    ptr -= 1
                else:
                    ptr -= 1
                    board[i][ptr] = tmp
    return board


def dfs(board, cnt):
    if cnt == 5:
        return max(map(max, board))
    return max(dfs(up(deepcopy(board)), cnt + 1), dfs(down(deepcopy(board)), cnt + 1),
               dfs(left(deepcopy(board)), cnt + 1),
               dfs(right(deepcopy(board)), cnt + 1), )


print(dfs(board, 0))
