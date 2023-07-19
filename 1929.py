import sys

input = sys.stdin.readline

m, n = map(int, input().split())


def is_prime(a):
    if a < 2:
        return False
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True


for x in range(m, n + 1):
    if is_prime(x):
        print(x)
