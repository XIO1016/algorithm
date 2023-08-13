import sys

input = sys.stdin.readline

n = int(input())


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


ans = 0
while True:
    if str(n) == str(n)[::-1]:
        if is_prime(n):
            ans = n
            break
    else:
        n += 1
print(ans)
