import sys
from collections import defaultdict

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]

dict = defaultdict(int)
dict[c] += 1

left, right = 0, k - 1
for i in range(k):
    dict[arr[i]] += 1

ans = -1

while left < N:
    ans = max(ans, len(dict))
    dict[arr[left]] -= 1
    if dict[arr[left]] == 0:
        del dict[arr[left]]
    left += 1
    right += 1
    dict[arr[right % N]] += 1
