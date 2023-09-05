import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

result = 0
idx = 0

for i in range(n):
    if arr[i][1] > result:
        result = arr[i][1]
        idx = i

height = arr[0][1]

for i in range(idx):
    result += height * (arr[i + 1][0] - arr[i][0])
    height = max(height, arr[i + 1][1])

height = arr[n - 1][1]

for i in range(n - 1, idx, -1):
    result += height * (arr[i][0] - arr[i - 1][0])
    height = max(height, arr[i - 1][1])

print(result)
