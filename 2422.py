import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
ice = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    ice[a - 1][b - 1] = 1
    ice[b - 1][a - 1] = 1

ans = 0
for i in combinations(range(n), 3):
    if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
        continue
    ans += 1
print(ans)
