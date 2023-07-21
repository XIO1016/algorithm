import sys

input = sys.stdin.readline

mini, maxi = map(int, input().split())
ans = maxi - mini + 1
a = [True] * (maxi - mini + 1)
for i in range(2, int(maxi ** 0.5) + 1):
    sq = i ** 2
    for j in range((sq - (mini % sq)) % sq, len(a), sq):
        a[j] = False
print(sum(a))
