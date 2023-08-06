import sys

input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

ans = road[0] * oil[0]
mini = oil[0]

for i in range(1, n - 1):
    if mini > oil[i]:
        mini = oil[i]
    ans += mini * road[i]
print(ans)
