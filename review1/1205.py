import sys

input = sys.stdin.readline

n, new, p = map(int, input().split())

if n == 0:
    print(1)
    exit(0)

score = list(map(int, input().split()))

if n == p and score[-1] >= new:
    print(-1)
    exit(0)

for i in range(n):
    if score[i] <= new:
        print(i + 1)
        exit(0)

print(n + 1)
