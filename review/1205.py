import sys

input = sys.stdin.readline

n, new, p = map(int, input().split())

if n == 0:
    print(1)
    exit(1)
score = list(map(int, input().split()))

if n == p and score[-1] >= new:
    print(-1)
else:
    ans = n + 1
    for i in range(n):
        if score[i] <= new:
            ans = i + 1
            break
    print(ans)
