n, m = map(int, input().split())
lenArr = list(map(int, input().split()))

# 10 15 17 19
def binary_search(array, target, start, end):
    while start <= end:
        count = 0
        mid = (start + end) // 2

        for x in lenArr:
            if mid < x:
                count += (x - mid)

        if target == count:
            return mid
        # 떡의 양이 부족한 경우 : 더 많이 잘라야 한다. 왼쪽으로!
        elif target > count:
            end = mid - 1
        else:
            start = mid + 1
    return None

print(binary_search(lenArr, m, 0, max(lenArr)))
