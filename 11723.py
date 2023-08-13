import sys

input = sys.stdin.readline

t = int(input())
s = set()

for _ in range(t):
    x = list(input().strip().split())
    m = x[0]
    if m == 'add':
        s.add(int(x[1]))
    elif m == 'remove':
        s.discard(int(x[1]))
    elif m == 'check':
        if int(x[1]) in s:
            print(1)
        else:
            print(0)
    elif m == 'toggle':
        if int(x[1]) in s:
            s.discard(int(x[1]))
        else:
            s.add(int(x[1]))
    elif m == 'all':
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif m == 'empty':
        s = set()
