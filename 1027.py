import sys

input = sys.stdin.readline


def calc(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


n = int(input())
arr = list(map(int, input().split()))
ans = 0

for idx, h in enumerate(arr):
    view = 0
    left = float("inf")
    right = -float("inf")
    for i in range(idx - 1, -1, -1):
        c = calc(idx + 1, h, i + 1, arr[i])
        if c < left:
            left = c
            view += 1
    for i in range(idx + 1, n):
        c = calc(idx + 1, h, i + 1, arr[i])
        if c > right:
            right = c
            view += 1
    ans = max(ans, view)
print(ans)
