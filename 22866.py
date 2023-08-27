import sys

input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))
INF = float("inf")

building_cnt = [0] * n
near = [INF] * n

left = []
for i, h in enumerate(height):
    while left and height[left[-1]] <= h:
        left.pop()
    building_cnt[i] += len(left)
    if left:
        if abs(i - left[-1]) < abs(near[i] - i):
            near[i] = left[-1]
    left.append(i)

right = []
for i in range(n - 1, -1, -1):
    h = height[i]
    while right and height[right[-1]] <= h:
        right.pop()
    building_cnt[i] += len(right)
    if right:
        if abs(i - right[-1]) < abs(near[i] - i):
            near[i] = right[-1]
    right.append(i)

for i in range(n):
    if building_cnt[i]:
        print(building_cnt[i], near[i] + 1)
    else:
        print(0)
