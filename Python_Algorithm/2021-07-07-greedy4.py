# 실패
n = int(input())
array_unit = list(map(int, input().split()))
sum = 0
sum_result = []

for unit in array_unit:
    if unit not in sum_result:
        sum_result.append(unit)

for i in range(len(array_unit)):
    for j in range(i + 1, len(array_unit)):
        sum = array_unit[i] + array_unit[j]
        if sum not in sum_result:
            sum_result.append(sum)
        else:
            continue
sum_result.sort()
print(sum_result)
