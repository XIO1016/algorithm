import sys

input = sys.stdin.readline

n = int(input())

arr = [0, 0] + [1] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if arr[i]:
        arr[i * 2::i] = [0] * ((n - i) // i)

a = []
for i in range(n + 1):
    if arr[i]:
        a.append(i)

left, right = 0, 0
ans = 0
while left <= right:
    temp = sum(arr[left:right])
    if temp == n:
        ans += 1
        right += 1
    elif temp < n:
        right += 1
    else:
        left += 1
print(ans)
