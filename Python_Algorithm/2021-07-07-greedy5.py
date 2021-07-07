n, m = map(int, input().split())
array_k = list(map(int, input().split()))
count = 0

for i in range(0, n):
    for j in range(i + 1, n):
        if array_k[i] == array_k[j]:
            continue
        else:
            count += 1

print(count)
