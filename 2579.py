import sys

input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]
d = [0] * n
if n <= 2:
    print(sum(score))
else:
    d[0] = score[0]
    d[1] = score[0] + score[1]
    for i in range(2, n):
        d[i] = max(d[i - 3] + score[i - 1] + score[i], d[i - 2] + score[i])
    print(d[-1])
