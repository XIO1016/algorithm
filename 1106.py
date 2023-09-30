import sys

input = sys.stdin.readline
c, n = map(int, input().split())
d = [1e9] * (c + 100)
arr = [list(map(int, input().split())) for _ in range(n)]
d[0] = 0
for cost, people in arr:
    for i in range(people, c + 100):
        d[i] = min(d[i - people] + cost, d[i])
print(min(d[c:]))
