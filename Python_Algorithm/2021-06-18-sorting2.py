n = int(input())
array =[]

for _ in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, reverse=False, key = lambda x : x[1])

for i in range(n):
    print(array[i][0], end=' ')
