def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        number[a] += number[b]


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


for _ in range(int(input())):
    f = int(input())
    parent, number = {}, {}
    for _ in range(f):
        a, b = input().strip().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)
        print(number[find(a)])
