n = int(input())
table = []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    table.append(list(map(int, input().split())))

for i in range(n - 1, -1, -1):
    time = table[i][0] + i
    if time <= n:
        dp[i] = max(table[i][1] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)

# 6 5 4  3  2  1  0  > i
# 8 9 6  4  3  6  3  > time
# 0 0 15 35 45 45 45 > dp
# dp[6] = 0
# dp[5] = 0
# dp[4] = max(table[4][1] + dp[6], 0) = 15
# dp[3] = max(table[3][1] + dp[4], 15) = 35
# dp[2] = max(table[2][1] + dp[3], 35) = 45
# dp[1] = max(table[1][1] + dp[6], 45) = 45
# dp[0] = max(table[0][1] + dp[3], 45) = 45