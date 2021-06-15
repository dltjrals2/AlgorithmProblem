n = int(input()) # 공간의 크기 입력 받기
move = list(map(str, input().split())) # 이동할 계획서 내용 입력 받기
length = len(move)
now_pos = [1, 1]

for moving in move:
    if moving == "L":
        if now_pos[1] == 1:
            continue
        else:
            now_pos[1] -= 1
    elif moving == "R":
        if now_pos[1] == n:
            continue
        else:
            now_pos[1] += 1
    elif moving == "U":
        if now_pos[0] == 1:
            continue
        else:
            now_pos[0] -= 1
    else:
        if now_pos[0] == n:
            continue
        else:
            now_pos[0] += 1

print(now_pos)
