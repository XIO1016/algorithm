import sys

input = sys.stdin.readline

n = int(input())


def check(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


while True:
    if str(n)[-1::-1] == str(n):
        if check(n):
            print(n)
            break
    n += 1
