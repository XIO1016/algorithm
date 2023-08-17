import sys

input = sys.stdin.readline

n, m = map(int, input().split())
word = {input().strip(): 1 for _ in range(n)}

res = n
for _ in range(m):
    a = list(input().strip().split(','))
    for i in a:
        if i in word.keys():
            if word[i] == 1:
                word[i] -= 1
                res -= 1
    print(res)
