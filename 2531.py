import sys
from collections import defaultdict

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]

left, right = 0, k - 1
ans = -1

dict = defaultdict(int)

dict[c] += 1

for i in range(right + 1):
    dict[arr[i]] += 1

while left < N:
    ans = max(len(dict), ans)
    dict[arr[left]] -= 1
    if dict[arr[left]] == 0:
        del dict[arr[left]]
    left += 1

    right += 1
    dict[arr[right % N]] += 1
print(ans)
