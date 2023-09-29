n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, j):
        d[i] = max(d[i], d[j] + d[i - j])
print(d[n])
