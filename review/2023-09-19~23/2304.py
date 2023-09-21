import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()
ans = 0
idx = 0
for i in range(n):
    if ans < arr[i][1]:
        ans = arr[i][1]
        idx = i

height = arr[0][1]

for i in range(idx):
    ans += height * (arr[i + 1][0] - arr[i][0])
    if height < arr[i + 1][1]:
        height = arr[i + 1][1]

height = arr[-1][1]

for i in range(n - 1, idx, -1):
    ans += height * (arr[i][0] - arr[i - 1][0])
    if height < arr[i - 1][1]:
        height = arr[i - 1][1]
print(ans)
