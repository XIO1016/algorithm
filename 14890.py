import sys

input = sys.stdin.readline

n, l = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def check_line(line):
    for i in range(1, n):
        if abs(line[i] - line[i - 1]) > 1:
            return False
        if line[i] < line[i - 1]:
            for j in range(l):
                if i + j >= n or slope[i + j] or line[i] != line[i + j]:
                    return False
                if line[i] == line[i + j]:
                    slope[i + j] = 1
        elif line[i] > line[i - 1]:
            for j in range(l):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or slope[i - j - 1]:
                    return False
                if line[i - 1] == line[i - j - 1]:
                    slope[i - j - 1] = 1
    return True


for i in range(n):
    slope = [0] * n
    if check_line(graph[i]):
        ans += 1
for i in range(n):
    slope = [0] * n
    if check_line([graph[j][i] for j in range(n)]):
        ans += 1

print(ans)
