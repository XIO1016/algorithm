import sys

input = sys.stdin.readline

arr = []

a = [False, False] + [True] * 1000000
for i in range(2, 1001):
    if a[i]:
        for j in range(2 * i, 1000001, i):
            a[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    check = -1
    for i in range(3, n, 2):
        if a[i] and a[n - i]:
            print(n, "=", i, "+", n - i)
            check = 1
            break

    if check == -1:
        print("Goldbach's conjecture is wrong.")
