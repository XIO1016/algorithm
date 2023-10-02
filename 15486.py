import sys

input = sys.stdin.readline
n = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
d = [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = max(d[i], d[i - 1])
    final = i + arr[i][0] - 1
    if final <= n:
        d[final] = max(d[final], d[i - 1] + arr[i][1])
print(max(d))
