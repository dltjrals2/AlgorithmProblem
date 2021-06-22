x = int(input())
result = 0
while x != 1:
    print(x)
    if x % 5 == 0:
        x = x // 5
    elif x % 3 == 0:
        x = x // 3
    elif x % 2 == 0:
        x = x // 2
    else:
        x = x - 1
    result += 1
print(result)
