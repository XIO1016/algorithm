import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

parent = [i for i in range(n)]


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


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)

parent = [-1] + parent
trip = list(map(int, input().split()))

start = parent[trip[0]]

for i in range(1, m):
    if start != parent[trip[i]]:
        print("NO")
        break
else:
    print("YES")
