import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n - 1

ans = float("inf")
a, b = 0, 0

while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) < ans:
        a, b = arr[left], arr[right]
        ans = abs(temp)
    if temp == 0:
        break
    elif temp < 0:
        left += 1
    else:
        right += 1
print(a, b)
