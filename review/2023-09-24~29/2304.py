n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()

ans = 0
index = 0
for i in range(n):
    if arr[i][1] > ans:
        ans = arr[i][1]
        index = i

height = arr[0][1]
for i in range(index):
    ans += height * (arr[i + 1][0] - arr[i][0])
    height = max(height, arr[i + 1][1])

height = arr[n - 1][1]
for i in range(n - 1, index, -1):
    ans += height * (arr[i][0] - arr[i - 1][0])
    height = max(height, arr[i - 1][1])
print(ans)
