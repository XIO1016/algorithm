import sys

input = sys.stdin.readline
n = int(input())
d = [0] * (n + 1)
d[0] = 1
for i in range(1, n + 1):
    tmp = 0
    for j in range(i + 1):
        tmp += d[j] * d[i - j - 1]
    d[i] = tmp
print(d[-1])
