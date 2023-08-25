import sys

input = sys.stdin.readline

k = int(input())
arr = list(input().strip().split())


def check(a, b, c):
    if c == "<":
        return a < b
    else:
        return a > b


visited = [0] * 10

ans1, ans2 = '', ''


def recursive(num, idx):
    global ans1, ans2
    if idx == k + 1:
        if ans1 == '':
            ans1 = num
        else:
            ans2 = num
        return
    for i in range(10):
        if visited[i] == 0:
            if idx == 0 or check(num[-1], str(i), arr[idx - 1]):
                visited[i] = 1
                recursive(num + str(i), idx + 1)
                visited[i] = 0


recursive('', 0)
print(ans2)
print(ans1)
