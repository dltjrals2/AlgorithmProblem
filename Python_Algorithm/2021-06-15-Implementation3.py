position = input()
row = int(position[1])
column = int(ord(position[0])) - int(ord('a')) + 1

move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
count = 0

for moving in move:
    next_row = row + moving[0]
    next_column = column + moving[1]
    if next_row < 1 or next_row > 8 or next_column < 1 or next_column > 8:
        continue
    count += 1

print(count)
