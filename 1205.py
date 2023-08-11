import sys

input = sys.stdin.readline

n, new, p = map(int, input().split())
curr = list(map(int, input().split()))

if n == 0:
    print(1)
else:
    if n == p and curr[-1] >= new:
        print(-1)
    else:
        ans = n + 1
        for i in range(n):
            if curr[i] <= new:
                ans = i + 1
                break
        print(ans)
