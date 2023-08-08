import sys

input = sys.stdin.readline

n = int(input())

arr = [0, 0] + [1] * (n - 1)
prime = []
for i in range(2, int(n ** 0.5) + 1):
    if arr[i]:
        arr[i * 2::i] = [0] * ((n - i) // i)
for i in range(n + 1):
    if arr[i]:
        prime.append(i)
ans = 0
left, right = 0, 0
while right <= len(prime):
    temp = sum(prime[left:right])
    if temp == n:
        ans += 1
        right += 1
    elif temp < n:
        right += 1
    else:
        left += 1

print(ans)
