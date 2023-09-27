import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l = []
    r = []
    data = input().strip()
    for a in data:
        if a == '-':
            if l:
                l.pop()
        elif a == '<':
            if l:
                r.append(l.pop())
        elif a == '>':
            if r:
                l.append(r.pop())
        else:
            l.append(a)
    l.extend(reversed(r))
    print(''.join(l))
