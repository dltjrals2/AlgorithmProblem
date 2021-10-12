house_number = int(input())
house_list = list(map(int, input().split()))
house_list.sort()

print(house_list[(house_number - 1) // 2])