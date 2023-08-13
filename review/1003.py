import sys

input = sys.stdin.readline

zero = [1, 0, 1] + [0] * (40)
one = [0, 1, 1] + [0] * 40

t = int(input())


def fibonacci(n):
    if n > 2:
        for i in range(3, n + 1):
            zero[i] = zero[i - 1] + zero[i - 2]
            one[i] = one[i - 1] + one[i - 2]


for _ in range(t):
    x = int(input())
    if x < 3:
        print(zero[x], one[x])
    else:
        fibonacci(x)
        print(zero[x], one[x])
