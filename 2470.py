import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = abs(arr[0] + arr[-1])
left, right = 0, n - 1
a, b = arr[0], arr[-1]
while left < right:
    tmp = arr[left] + arr[right]
    if abs(tmp) < ans:
        ans = abs(tmp)
        a = arr[left]
        b = arr[right]
        if ans == 0:
            break
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(a, b)
