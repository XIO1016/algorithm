import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    person = [list(map(int, input().split())) for _ in range(n)]
    person.sort()
    ans = 1
    top = 0
    for i in range(1, n):
        if person[i][1] <= person[top][1]:
            ans += 1
            top = i
    print(ans)
