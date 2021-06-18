n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)
while array:
    print(array.pop(0), end = ' ')
