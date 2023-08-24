import sys

input = sys.stdin.readline

k = int(input())
arr = list(input().strip().split())


def check(a, b, c):
    if c == '<':
        return a < b
    else:
        return b > a


visited = [0] * 10
m, n = '', ''


def recursive(idx, num):
    global m, n
    if idx == k + 1:
        if len(m) == 0:
            m = num
        else:
            n = num
        return
    for i in range(10):
        if visited[i] == 0:
            if idx == 0 or check(num[1], str(i), arr[idx - 1]):
                visited[i] = 1
                recursive(idx + 1, num + str(i))
                visited[i] = 0
