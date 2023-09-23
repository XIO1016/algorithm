import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def sol(lst):
    total = 0
    for i in range(n - 1):
        total += abs(lst[i] - lst[i + 1])
    return total


ans = 0
for a in list(permutations(arr, n)):
    ans = max(ans, sol(a))
print(ans)
