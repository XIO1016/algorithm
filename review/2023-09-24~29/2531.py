from collections import defaultdict

N, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(N)]
left, right = 0, k - 1

dic = defaultdict(int)
dic[c] = 1
for i in range(k):
    dic[arr[i]] += 1

ans = -1
while left < N:
    ans = max(ans, len(dic))
    dic[arr[left]] -= 1
    if dic[arr[left]] == 0:
        del dic[arr[left]]
    left += 1
    right += 1
    dic[arr[right % N]] += 1
print(ans)
