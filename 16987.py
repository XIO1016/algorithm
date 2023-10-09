import sys

input = sys.stdin.readline
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def back_tracking(start):
    global ans
    if start == n:
        total = 0
        for i in range(n):
            if eggs[i][0] <= 0:
                total += 1
        ans = max(ans, total)
        return
    if eggs[start][0] <= 0:
        back_tracking(start + 1)
        return
    flag = True  # 다깨짐
    for i in range(n):
        if eggs[i][0] > 0 and i != start:
            flag = False
            eggs[i][0] -= eggs[start][1]
            eggs[start][0] -= eggs[i][1]
            back_tracking(start + 1)
            eggs[i][0] += eggs[start][1]
            eggs[start][0] += eggs[i][1]
        if flag:
            back_tracking(n)


back_tracking(0)

print(ans)
