import sys

input = sys.stdin.readline

n = int(input())


def check(a):
    for i in range(1, len(a) // 2 + 1):
        if a[-i:] == a[-(2 * i):-i]:
            return False
    return True


def recursive(num):
    if len(num) == n:
        print(num)
        exit(0)
    for i in '123':
        if check(num + i):
            recursive(num + i)


recursive('1')
