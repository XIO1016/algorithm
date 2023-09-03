import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n - 1
a, b = 0, 0

ans = float("inf")

while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) < ans:
        ans = abs(temp)
        a, b = arr[left], arr[right]
    if temp == 0:
        break
    elif temp > 0:
        right -= 1
    else:
        left += 1
print(a, b)
