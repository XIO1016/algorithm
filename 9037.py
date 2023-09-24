import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    cnt = 0
    while True:
        c = [i if i % 2 == 0 else i + 1 for i in c]
        if len(set(c)) == 1:
            print(cnt)
            break
        c = [c[i] // 2 + c[(i + 1) % n] // 2 for i in range(n)]
        cnt += 1
