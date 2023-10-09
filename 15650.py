import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ans = []


def back_tracking(start):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(start, n + 1):
        if i not in ans:
            ans.append(i)
            back_tracking(i + 1)
            ans.pop()


back_tracking(1)
