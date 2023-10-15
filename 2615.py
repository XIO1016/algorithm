graph = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if graph[x][y] != 0:
            focus = graph[x][y]
            for i in range(4):
                cnt = 1
                nx, ny = x + dx[i], y + dy[i]
                while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == focus:
                    cnt += 1
                    if cnt == 5:
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and graph[x - dx[i]][y - dy[i]] == focus:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and graph[nx + dx[i]][ny + dy[i]] == focus:
                            break
                        print(focus)
                        print(x + 1, y + 1)
                        exit()
                    nx += dx[i]
                    ny += dy[i]
print(0)
