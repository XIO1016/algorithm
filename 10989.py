import sys

input = sys.stdin.readline
n = int(input())
arr = [0] * 10001
for _ in range(n):
    arr[int(input())] += 1
for i in range(10001):
    if not arr[i] == 0:
        for j in range(arr[i]):
            print(i)
