import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    arr.sort(key=lambda x: (x[1], x[0]))
    cnt = 0
    visited = [0] * (n + 1)
    for a, b in arr:
        for i in range(a, b + 1):
            if not visited[i]:
                visited[i] += 1
                cnt += 1
                break
    print(cnt)
