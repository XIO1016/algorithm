import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left, right = 0, k - 1
ans = -1

dic = defaultdict(int)
dic[c] += 1

for i in range(k):
    dic[arr[i]] += 1

while left < n:
    ans = max(len(dic), ans)
    dic[arr[left]] -= 1
    if dic[arr[left]] == 0:
        del dic[arr[left]]
    left += 1
    right += 1
    dic[arr[right % n]] += 1
print(ans)
