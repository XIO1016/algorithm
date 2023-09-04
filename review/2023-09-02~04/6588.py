import sys

input = sys.stdin.readline

arr = [0, 0] + [1] * (1000001 - 2)

for i in range(2, int(1000001 ** 0.5) + 1):
    if arr[i]:
        for j in range(i * 2, 1000001, i):
            arr[j] = 0
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n, 2):
        if arr[i] and arr[n - i]:
            print(n, "=", i, "+", n - i)
            break
