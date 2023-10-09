import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []


def back_tracking(start):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(start, n + 1):
        if arr[i - 1] not in ans:
            ans.append(arr[i - 1])
            back_tracking(i)
            ans.pop()


back_tracking(1)
