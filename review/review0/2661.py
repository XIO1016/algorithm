import sys

input = sys.stdin.readline

n = int(input())


def check(a):
    for i in range(1, len(a) // 2 + 1):
        if a[-i:] == a[-(i * 2):-i]:
            return False
    return True


def recursive(a):
    if len(a) == n:
        print(a)
        exit(1)
    for i in '123':
        if check(a + i):
            recursive(a + i)
    return


recursive('')
