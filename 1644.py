import sys

input = sys.stdin.readline

n = int(input())

arr = []
a = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if a[i]:
        a[i * 2::i] = [False] * ((n - i) // i)

for i in range(n + 1):
    if a[i]:
        arr.append(i)

ans = 0
left, right = 0, 0
while right <= len(arr):
    temp = sum(arr[left:right])
    if temp == n:
        ans += 1
        right += 1
    elif temp < n:
        right += 1
    else:
        left += 1

print(ans)
