import math
import sys

input = sys.stdin.readline
n = int(input())
d = [0, 1]

for i in range(2, n + 1):
    mn = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        mn = min(mn, d[i - j ** 2])
    d.append(mn + 1)

print(d[n])
