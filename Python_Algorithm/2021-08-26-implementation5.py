n, m = map(int, input().split())
chicken_map = [[0] * n for _ in range(n)]


for i in range(n):
    chicken_map[i] = list(map(int, input().split()))

def solution(n, m, chicken_map):
    house_info = list()
    chicken_info = list()
    num = 0

    for i in range(n):
        for j in range(n):
            # 집인 경우
            if chicken_map[i][j] == 1:
                house_info.append([i + 1, j + 1])
            # 치킨 집인 경우
            elif chicken_map[i][j] == 2:
                chicken_info.append([i + 1, j + 1])
                num += 1
    # 폐업하는 가게의 수
    close_door = num - m
    print(close_door)

    searchMinDistance(house_info, chicken_info, close_door)

def searchMinDistance(house_info, chicken_info, close_door):
    min_distance = 0
    sum_list = list()

    for house in house_info:
        min_value = 99999
        for chicken in chicken_info:
            min_distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            if min_distance < min_value:
                min_value = min_distance
        sum_list.append(min_value)

    print(sum(sum_list))

solution(n, m, chicken_map)
