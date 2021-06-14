# 숫자 카드 게임
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 9999
    for value in data:
        min_value = min(min_value, value)
    result = max(result, min_value)

print(result)
