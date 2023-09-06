import copy
import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]


def rotate(board):
    temp = copy.deepcopy(board)
    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = board[i][j]
    return temp


def dfs(board, cnt):
    a = max([max(i) for i in board])
    if cnt == 0:
        return a
    for _ in range(4):
        tmp = [convert(i) for i in board]
        if board != tmp:
            a = max(a, dfs(tmp, cnt - 1))
        board = rotate(board)
    return a


def convert(lst):
    tmp = [i for i in lst if i]
    for i in range(1, len(tmp)):
        if tmp[i - 1] == tmp[i]:
            tmp[i - 1] = tmp[i] * 2
            tmp[i] = 0
    tmp = [i for i in tmp if i]
    return tmp + ([0] * (n - len(tmp)))


print(dfs(board, 5))
