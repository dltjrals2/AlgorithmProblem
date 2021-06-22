# 가로의 길이가 N, 세로의 길이가 2
n = int(input()) # (1 <= n <= 1,000)
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + (d[i - 2] * 2)) % 796796

print(d[n])
