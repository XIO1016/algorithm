import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
cnt = 0


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if (a % i) == 0:
            return False
    return True


for l in lst:
    if is_prime(l):
        cnt += 1
print(cnt)
