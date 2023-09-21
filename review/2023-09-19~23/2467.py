import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

ans = int(1e9)
a = 0
b = 0
left, right = 0, n - 1
while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) < ans:
        ans = abs(temp)
        a = arr[left]
        b = arr[right]
    if temp == 0:
        break
    elif temp > 0:
        right -= 1
    else:
        left += 1

print(a, b)
