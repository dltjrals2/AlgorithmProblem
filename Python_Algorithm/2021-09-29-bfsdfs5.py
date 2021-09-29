n = int(input())
array = list(map(int, input().split()))
operator = list(map(int, input().split()))

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, operator
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if operator[0] > 0:
            operator[0] -= 1
            dfs(i + 1, now + array[i])
            operator[0] += 1
        if operator[1] > 0:
            operator[1] -= 1
            dfs(i + 1, now - array[i])
            operator[1] += 1
        if operator[2] > 0:
            operator[2] -= 1
            dfs(i + 1, now * array[i])
            operator[2] += 1
        if operator[3] > 0:
            operator[3] -= 1
            dfs(i + 1, int(now / array[i]))
            operator[3] += 1

dfs(1, array[0])

print(max_value)
print(min_value)