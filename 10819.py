import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))


def sol(lst):
    total = 0
    for i in range(n - 1):
        total += abs(lst[i] - lst[i + 1])
    return total


ans = 0
for i in list(permutations(a, n)):
    ans = max(ans, sol(i))

print(ans)
