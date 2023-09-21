import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, m):
    arr[0][i] += arr[0][i - 1]

for i in range(1, n):
    lr = arr[i][:]
    rl = arr[i][:]
    for j in range(m):
        if j == 0:
            lr[j] += arr[i - 1][j]
        else:
            lr[j] += max(lr[j - 1], arr[i - 1][j])
    for j in range(m - 1, -1, -1):
        if j == m - 1:
            rl[j] += arr[i - 1][j]
        else:
            rl[j] += max(rl[j + 1], arr[i - 1][j])
    for j in range(m):
        arr[i][j] = max(rl[j], lr[j])

print(arr[n - 1][m - 1])
