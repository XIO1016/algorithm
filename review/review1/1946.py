import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    score.sort()
    top = 0
    cnt = 1
    print(score)
    for i in range(1, n):
        if score[i][1] <= score[top][1]:
            top = i
            cnt += 1