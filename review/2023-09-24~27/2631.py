n = int(input())

arr = [0] + [int(input()) for _ in range(n)]

d = [1] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + 1)
            print(d)
print(n - max(d))
