import sys

input = sys.stdin.readline

arr = list(input().strip().upper())
num = {}
for i in arr:
    try:
        num[i] += 1
    except:
        num[i] = 1
ans = max(num.values())
answer = []
for k, v in num.items():
    if v == ans:
        answer.append(k)
if len(answer) != 1:
    print("?")
else:
    print(answer[0].upper())
