import sys
from itertools import combinations

input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
for x in combinations(arr, 7):
    if sum(x) == 100:
        x = list(x)
        x.sort()
        print("\n".join(map(str, x)))
        break
