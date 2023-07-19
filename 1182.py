import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in combinations(lst, i + 1):
        if sum(j) == s:
            cnt += 1

print(cnt)
