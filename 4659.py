import sys

input = sys.stdin.readline


def check(s):
    if s in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False


def check1(s):
    for i in s:
        if check(i):
            return True
    return False


def check2(s):
    for i in range(1, len(s) - 1):
        if check(s[i - 1]) and check(s[i]) and check(s[i + 1]):
            return False
        elif not check(s[i - 1]) and not check(s[i]) and not check(s[i + 1]):
            return False
    return True


def check3(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and not (s[i] == 'e' or s[i] == 'o'):
            return False
    return True


while True:
    x = input().strip()
    if x == "end":
        break
    if check1(x) and check2(x) and check3(x):
        print("<{0}> is acceptable.".format(x))
    else:
        print("<{0}> is not acceptable.".format(x))
