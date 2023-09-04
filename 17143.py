import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())
graph = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r - 1][c - 1] = (s, d, z)

up, down, right, left = 1, 2, 3, 4


def fish(j):
    for i in range(R):
        if graph[i][j]:
            x = graph[i][j][2]
            graph[i][j] = 0
            return x
    return 0


def move():
    global graph
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                ni, nj, nd = get_next(i, j, graph[i][j][0], graph[i][j][1])
                if temp[ni][nj]:
                    temp[ni][nj] = max(
                        temp[ni][nj],
                        (graph[i][j][0], nd, graph[i][j][2]),
                        key=lambda x: x[2]
                    )
                else:
                    temp[ni][nj] = (graph[i][j][0], nd, graph[i][j][2])
    graph = temp


def get_next(i, j, speed, dir):
    if dir == up or dir == down:
        cycle = R * 2 - 2
        if dir == up:
            speed += 2 * (R - 1) - i
        else:
            speed += i
        speed %= cycle
        if speed >= R:
            return 2 * R - 2 - speed, j, up
        return speed, j, down
    else:
        cycle = C * 2 - 2
        if dir == left:
            speed += 2 * (C - 1) - j
        else:
            speed += j
        speed %= cycle
        if speed >= C:
            return i, 2 * C - 2 - speed, left
        return i, speed, right


ans = 0
for j in range(C):
    ans += fish(j)
    move()

print(ans)
