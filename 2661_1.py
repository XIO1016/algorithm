import sys

input = sys.stdin.readline

n = int(input())


def check(num):
    for i in range(1, len(num) // 2 + 1):
        if num[-i:] == num[-(i * 2):-i]:
            return False
    return True


def recursive(num):
    if len(num) == n:
        print(num)
        exit(1)
    for i in '123':
        if check(num + str(i)):
            recursive(num + str(i))


recursive('1')
