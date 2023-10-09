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
    for i in range(1, n + 1):
        if visited[i] == 0 and pre != arr[i - 1]:
            ans.append(arr[i - 1])
            pre = arr[i - 1]
            visited[i] = 1
            back_tracking()
            ans.pop()
            visited[i] = 0


back_tracking()
