import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [0] * (n + 1)


def back_tracking(start):
    pre = 0
    if len(ans) == m:
        print(*ans)
        return
    for i in range(start, n):
        if visited[i] == 0 and arr[i] != pre:
            visited[i] = 1
            pre = arr[i]
            ans.append(arr[i])
            back_tracking(i + 1)
            ans.pop()
            visited[i] = 0


back_tracking(0)
