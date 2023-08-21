import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = input().strip()
    k = int(input())

    d = defaultdict(list)
    for i, c in enumerate(w):
        if w.count(c) >= k:
            d[c].append(i)

    short = 10e7
    long = 0
    for c, lst in d.items():
        if len(lst) == k:
            length = lst[-1] - lst[0] + 1
            short = min(short, length)
            long = max(long, length)
        elif len(lst) > k:
            left = 0
            while True:
                right = left + k - 1
                length = lst[right] - lst[left] + 1
                short = min(short, length)
                long = max(long, length)
                if right == len(lst) - 1:
                    break
                left += 1
    if long == 0 and short == 10e7:
        print(-1)
    else:
        print(short, long)
