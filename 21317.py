from copy import deepcopy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n - 1)]
k = int(input())

if n == 1:
    print(0)
    exit()
elif n == 2:
    print(arr[0][0])
    exit()

d = [0] * n
d[1] = arr[0][0]

d[2] = min(arr[1][0] + arr[0][0], arr[0][1])

for i in range(3, n):
    d[i] = min(arr[i - 2][1] + d[i - 2], arr[i - 1][0] + d[i - 1])
ans = d[-1]
d2 = d[:]
for i in range(0, n - 3):
    if d[i] + k < d[i + 3]:
        d2[i + 3] = d[i] + k
        for j in range(i + 4, n):
            d2[j] = min(d[j], d2[j - 1] + arr[j - 1][0], d2[j - 2] + arr[j - 2][1])
        ans = min(d2[-1], ans)
print(ans)
