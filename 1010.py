import sys


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(m - n) * factorial(n)))
