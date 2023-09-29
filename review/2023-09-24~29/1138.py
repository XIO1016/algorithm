n = int(input(()))

arr = list(map(int, input().split()))

ans = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if ans[j] == 0 and cnt == arr[i]:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            cnt += 1
print(*ans)
