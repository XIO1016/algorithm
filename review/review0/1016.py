import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ans = m - n + 1
a = [1] * ans
for i in range(2, int(m ** 0.5) + 1):
    sq = i ** 2
    for j in range((sq - (n - sq)) % sq, len(a), sq):
        a[j] = 0
print(sum(a))
