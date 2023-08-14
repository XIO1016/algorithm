import sys

input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))
m = int(input())
student = [list(map(int, input().split())) for _ in range(m)]
for s in student:
    if s[0] == 1:
        for i in range(n):
            if (i + 1) % s[1] == 0:
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0
    else:
        i = 1
        while True:
            if 0 <= s[1] - i - 1 and s[1] + i - 1 < n and switch[s[1] - i - 1] == switch[s[1] + i - 1]:
                i += 1
            else:
                i = i - 1
                for j in range(s[1] - i - 1, s[1] + i):
                    if switch[j] == 0:
                        switch[j] = 1
                    else:
                        switch[j] = 0
                break
for i in range(n):
    print(switch[i], end=' ')
    if i % 20 == 19:
        print()
