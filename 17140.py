import sys
from collections import Counter
from functools import reduce

input = sys.stdin.readline


def R(arr):
    max_length = 0
    for i in range(len(arr)):
        X = Counter(arr[i])
        del X[0]
        X = list(X.items())
        X.sort(key=lambda x: (x[1], x[0]))
        if len(X) > 50:
            X = X[:50]
        arr[i] = reduce(lambda x, y: list(x) + list(y), X[1:], list(X[0]))
        max_length = max(max_length, len(arr[i]))
    for i in range(len(arr)):
        if len(arr[i]) < max_length:
            arr[i].extend([0] * (max_length - len(arr[i])))


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
time = 0
r, c = r - 1, c - 1
if r < len(A) and c < len(A[0]):
    if A[r][c] == k:
        print(time)
        exit()
while True:
    if len(A) >= len(A[0]):
        R(A)
    else:
        A = list(map(list, zip(*A)))
        R(A)
        A = list(map(list, zip(*A)))
    time += 1
    if time > 100:
        print(-1)
        exit()
    if r < len(A) and c < len(A[0]):
        if A[r][c] == k:
            print(time)
            exit()
