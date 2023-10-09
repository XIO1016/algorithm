import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []


def back_tracking():
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n + 1):
        if arr[i - 1] not in ans:
            ans.append(arr[i - 1])
            back_tracking()
            ans.pop()


back_tracking()
