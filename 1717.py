import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [0] + [i for i in range(1, n + 1)]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
