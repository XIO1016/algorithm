import sys

input = sys.stdin.readline

arr = [0, 0] + [1] * 100000
for i in range(2, int(100000 ** 0.5) + 1):
    if arr[i]:
        arr[2 * i::i] = [0] * ((100000 - i) // i)

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n, 2):
        if arr[i] and arr[n - i]:
            print(n, i, j)
            break
