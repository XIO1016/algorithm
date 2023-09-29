from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))
ans = -1
for i in list(permutations(arr, n)):
    tmp = 0
    for j in range(n - 1):
        tmp += abs(i[j] - i[j + 1])
    ans = max(ans, tmp)
print(ans)
