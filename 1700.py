import sys

input = sys.stdin.readline

n, k = map(int, input().split())

name = list(map(int, input().split()))

plug = []
cnt = 0

for i, item in enumerate(name):
    if item in plug:
        continue
    if len(plug) < n:
        plug.append(item)
    else:
        far = 0
        temp = 0
        for p in plug:
            if p not in name[i:]:
                temp = p
                break
            elif name[i:].index(p) > far:
                far = name[i:].index(p)
                temp = p
        plug[plug.index(temp)] = name[i]
        cnt += 1
print(cnt)
