import sys

input = sys.stdin.readline

n = int(input())

a = [0, 0] + [1] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if a[i]:
        a[i * 2::i] = [0] * ((n - i) // i)
arr = []
for i in range(len(a)):
    if a[i]:
        arr.append(i)

left, right = 0, 0
cnt = 0
while right <= len(arr):
    s = sum(arr[left:right])
    if s == n:
        cnt += 1
        right += 1
    elif s < n:
        right += 1
    else:
        left += 1

print(cnt)
