import copy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

direction = [[],
             [[0], [1], [2], [3]],
             [[0, 1], [2, 3]],
             [[0, 2], [2, 1], [1, 3], [3, 0]],
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]],
             [[0, 1, 2, 3]]]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def watch(x, y, direction, tmp):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] != 6:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
            else:
                break


def dfs(office, cnt):
    global ans
    tmp = copy.deepcopy(office)
    if cnt == cctv_cnt:
        c = 0
        for i in tmp:
            c += i.count(0)
        ans = min(ans, c)
        return
    x, y, cctv = q[cnt]
    for i in direction[cctv]:
        watch(x, y, i, tmp)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(office)


ans = float("inf")
office = []
q = []
cctv_cnt = 0
for i in range(n):
    temp = list(map(int, input().split()))
    office.append(temp)
    for j in range(len(temp)):
        if temp[j] != 0 and temp[j] != 6:
            cctv_cnt += 1
            q.append([i, j, temp[j]])

dfs(office, 0)
print(ans)
