import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())

ans = []


def back_tracking():
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            back_tracking()
            ans.pop()


back_tracking()
