from itertools import combinations

n, m = map(int, input().split())
house, chicken = [], []

for i in range(n):
    map_info = list(map(int, input().split()))
    for j in range(n):
        if map_info[j] == 1:
            house.append((i, j))
        elif map_info[j] == 2:
            chicken.append((i, j))

candidates = combinations(chicken, m)

def get_distance(candidate):
    distance = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        distance += temp
    return distance

temp = 1e9
for candidate in candidates:
    temp = min(temp, get_distance(candidate))
print(temp)
