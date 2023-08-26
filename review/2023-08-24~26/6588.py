import sys

input = sys.stdin.readline

arr = [0, 0] + [1] * (1000000)
for i in range(2, 1001):
    if arr[i]:
        arr[2 * i::i] = [0] * ((1000001 - i) // i)

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n, 2):
        if arr[i] and arr[n - i]:
            print(n, "=", i, "+", n - i)
            break
