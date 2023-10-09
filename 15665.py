import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [0] * (n + 1)


def back_tracking():
    pre = 0
    if len(ans) == m:
        print(*ans)
        return
    for i in range(n):
        if pre != arr[i]:
            pre = arr[i]
            ans.append(arr[i])
            back_tracking()
            ans.pop()


back_tracking()
