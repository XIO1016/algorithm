import sys
from itertools import combinations

input = sys.stdin.readline
n = list(input().strip())
ans = set()

stack = []
tmp = []
for i, a in enumerate(n):
    if a == "(":
        stack.append(i)
    elif a == ")":
        tmp.append((stack.pop(), i))

for i in range(1, len(tmp) + 1):
    c = combinations(tmp, i)
    for j in c:
        target = list(n)
        for k in j:
            target[k[0]] = ""
            target[k[1]] = ""
        ans.add(''.join(target))
for a in sorted(list(ans)):
    print(a)
