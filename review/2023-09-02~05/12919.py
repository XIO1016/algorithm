import sys

input = sys.stdin.readline
s = list(input().strip())
t = list(input().strip())


def recursive(a):
    if a == s:
        print(1)
        exit()
    if len(a) == 0:
        return 0
    if a[-1] == "A":
        recursive(a[:-1])
    if a[0] == "B":
        recursive(a[1:][::-1])


recursive(t)
print(0)
