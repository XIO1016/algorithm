import sys
from collections import deque

input = sys.stdin.readline


def check_right(x, dir):
    if x > 4 or gears[x - 1][2] == gears[x][6]:
        return

    if gears[x - 1][2] != gears[x][6]:
        check_right(x + 1, -dir)
        gears[x].rotate(dir)


def check_left(x, dir):
    if x < 1 or gears[x][2] == gears[x + 1][6]:
        return
    if gears[x + 1][6] != gears[x][2]:
        check_left(x - 1, -dir)
        gears[x].rotate(dir)


gears = {}
for i in range(1, 5):
    gears[i] = deque(list(map(int, list(input().strip()))))

k = int(input())
for _ in range(k):
    num, dirs = map(int, input().strip().split())
    check_right(num + 1, -dirs)
    check_left(num - 1, -dirs)
    gears[num].rotate(dirs)

ans = 0
for i in range(4):
    ans += (2 ** i) * gears[i + 1][0]
print(ans)
