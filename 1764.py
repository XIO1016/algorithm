import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for _ in range(n):
    d[input().strip()] = 1
ans = []
for _ in range(m):
    a = input().strip()
    if a in d:
        ans.append(a)
ans.sort()
print(len(ans))
print('\n'.join(ans))
