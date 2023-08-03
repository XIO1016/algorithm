import sys

input = sys.stdin.readline

k = int(input())

arr = list(input().strip().split())
visited = [0] * 10

max_ans = ""
min_ans = ""


def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j


def dfs(idx, num):
    global min_ans, max_ans
    if idx == k + 1:
        if len(min_ans) == 0:
            min_ans = num
        else:
            max_ans = num
        return
    for i in range(10):
        if visited[i] == 0:
            if idx == 0 or check(num[-1], str(i), arr[idx - 1]):
                visited[i] = True
                dfs(idx + 1, num + str(i))
                visited[i] = False


dfs(0, "")
print(max_ans)
print(min_ans)
