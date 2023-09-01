import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))

maxi = -1e9
mini = 1e9


def dfs(depth, total, plus, minus, multi, divi):
    global mini, maxi
    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    if plus:
        dfs(depth + 1, total + a[depth], plus - 1, minus, multi, divi)
    if minus:
        dfs(depth + 1, total - a[depth], plus, minus - 1, multi, divi)
    if multi:
        dfs(depth + 1, total * a[depth], plus, minus, multi - 1, divi)
    if divi:
        dfs(depth + 1, int(total / a[depth]), plus, minus, multi, divi - 1)


dfs(1, a[0], o[0], o[1], o[2], o[3])
print(maxi)
print(mini)
