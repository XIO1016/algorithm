import sys

input = sys.stdin.readline
n, m = map(int, input().split())


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


parent = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i + 1)
        exit()
    union(a, b)
print(0)
