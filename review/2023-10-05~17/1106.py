c, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [int(1e9)] * (c + 100)
dp[0] = 0
for cost, num in arr:
    for i in range(num, c + 100):
        dp[i] = min(dp[i - num] + cost, dp[i])
print(min(dp[c:]))
