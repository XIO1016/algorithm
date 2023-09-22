import copy
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

honey = copy.deepcopy(arr)
ans = 0

for i in range(1, n):
    honey[i] += honey[i - 1]

for i in range(1, n - 1):
    ans = max(ans, 2 * honey[-1] - arr[0] - arr[i] - honey[i])
for i in range(1, n - 1):
    ans = max(ans, honey[-1] - arr[-1] - arr[i] + honey[i - 1])
for i in range(1, n - 1):
    ans = max(ans, honey[i] - arr[0] + honey[-1] - honey[i - 1] - arr[-1])

print(ans)
