n, m = map(int, input().split())
lenArr = list(map(int, input().split()))
lenArr.sort()

# 10 15 17 19
def binary_search(array, target, start, end):
    while start <= end:
        count = 0
        mid = (start + end) // 2

        for i in range(start, end + 1):
            if mid < array[i]:
                count += (array[i] - mid)
            else:
                continue

        if target == count:
            return mid
        elif target > count:
            start = mid + 1
        else:
            end = mid - 1
    return None

print(binary_search(lenArr, m, 0, lenArr[-1]))
