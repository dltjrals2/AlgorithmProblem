# 큰 수의 법칙
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr, reverse=True)
cnt1 = 0
cnt2 = 0
sum = 0

while cnt1 < M:
    if cnt2 == K:
        sum += sorted_arr[1]
        cnt1 += 1
        cnt2 = 0
    else:
        sum += sorted_arr[0]
        cnt1 += 1
        cnt2 += 1

print(sum)
