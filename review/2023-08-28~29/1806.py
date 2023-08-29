import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
ans = float('inf')
a = 0
while True:
    if a >= s:
        ans = min(ans, right - left)
        a -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        a += arr[right]
        right += 1
if ans == float('inf'):
    print(0)
else:
    print(ans)
