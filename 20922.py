import sys

input = sys.stdin.readline

n, k = map(int, input().split())

a = list(map(int, input().split()))

left, right = 0, 0

counter = [0] * (max(a) + 1)

ans = 0
while right < n:
    if counter[a[right]] < k:
        counter[a[right]] += 1
        right += 1
    else:
        counter[a[left]] -= 1
        left += 1
    ans = max(right - left, ans)
print(ans)
