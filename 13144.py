import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = 0
left, right = 0, 0
dup = [0] * 100001

while left < n and right < n:
    if not dup[arr[right]]:
        dup[arr[right]] = 1
        right += 1
        result += right - left
    else:
        dup[arr[left]] = 0
        left += 1
print(result)
