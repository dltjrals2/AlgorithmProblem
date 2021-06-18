def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arrA[mid] == target:
        return mid
    elif arrA[mid] > target:
        return binary_search(arrA, target, start, mid - 1)
    else:
        return binary_search(arrA, target, mid + 1, end)

n = int(input())
arrA = list(map(int, input().split()))
arrA.sort()
m = int(input())
arrB = list(map(int, input().split()))

for i in arrB:
    result = binary_search(arrA, i, 0, n - 1)
    if result != None:
        print('Yes', end = ' ')
    else:
        print('No', end = ' ')
