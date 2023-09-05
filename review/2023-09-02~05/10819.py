import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0
for lst in list(permutations(a, n)):
    total = 0
    for i in range(n - 1):
        total += abs(lst[i] - lst[i + 1])
    ans = max(ans, total)

print(ans)
