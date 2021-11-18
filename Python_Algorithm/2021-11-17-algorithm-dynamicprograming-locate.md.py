n = int(input())
power = list(map(int, input().split()))
power.reverse()
dp = [1] * (n + 1)

for i in range(n):
    for j in range(0, i):
        if power[j] < power[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))