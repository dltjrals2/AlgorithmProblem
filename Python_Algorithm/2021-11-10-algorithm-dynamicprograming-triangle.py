n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

#Dynamic Programming
for i in range(1, n):
    for j in range(len(array[i])):
        # 왼쪽에서 오는 경우
        if j == 0:
            left = 0
        else:
            left = array[i - 1][j - 1]
        # 오른쪽에서 오는 경우
        if j == len(array[i]) - 1:
            right = 0
        else:
            right = array[i - 1][j]

        array[i][j] = array[i][j] + max(left, right)


result = 0
for i in range(n):
    for j in range(len(array[i])):
        result = max(result, array[i][j])

print(result)