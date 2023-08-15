import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(1, m):
    ans = max(ans, x[i] - x[i - 1])

print(max((ans + 1) // 2, x[0] - 0, n - x[-1]))
