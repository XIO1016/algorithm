import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort()
    result = 1
    top = 0
    for i in range(1, n):
        if rank[i][1] < rank[top][1]:
            result += 1
            top = i
    print(result)
