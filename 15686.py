import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

c_loc = []
h_loc = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            h_loc.append([i, j])
        elif city[i][j] == 2:
            c_loc.append([i, j])


def sol(c, h):
    sum_distance = 0
    for hi in h:
        min_distance = 99999
        for ci in c:
            min_distance = min(min_distance, abs(ci[0] - hi[0]) + abs(ci[1] - hi[1]))
        sum_distance += min_distance
    return sum_distance


if len(c_loc) == m:
    print(sol(c_loc, h_loc))
else:
    min_sum = 99999
    for x in combinations(c_loc, m):
        min_sum = min(min_sum, sol(x, h_loc))
    print(min_sum)
