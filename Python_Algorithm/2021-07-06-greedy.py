n = int(input())
people = list(map(int, input().split()))
people.sort()
num = people.pop()

if num == 1:
    result = 1
else:
    result = 0

while people:
    if num == 1:
        num = people.pop()

    else:
        for _ in range(num - 1):
            pop_num = people.pop()
            if pop_num > num:
                num = pop_num
    result += 1

print(result)
