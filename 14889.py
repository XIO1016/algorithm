import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]
member = [i for i in range(n)]

min_cnt = 99999

for start in combinations(member, n // 2):
    link = member.copy()
    for x in start:
        link.remove(x)
    start_cnt = 0
    link_cnt = 0
    for x in combinations(start, 2):
        start_cnt += S[x[0]][x[1]] + S[x[1]][x[0]]
    for x in combinations(link, 2):
        link_cnt += S[x[0]][x[1]] + S[x[1]][x[0]]
    min_cnt = min(min_cnt, abs(start_cnt - link_cnt))
print(min_cnt)
