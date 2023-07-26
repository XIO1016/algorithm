import sys

input = sys.stdin.readline

T = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(a):
    if a >= len(zero):
        for i in range(len(zero), a + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[a], one[a])


for _ in range(T):
    fibonacci(int(input()))
