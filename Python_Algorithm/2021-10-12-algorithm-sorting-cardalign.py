n = int(input())
card_list = list()

for _ in range(n):
    card_list.append(int(input()))

length = len(card_list)
card_list = sorted(card_list, reverse=False)

sum = 0
answer = 0
while length > 0:
    sum += card_list.pop(0)
    sum += card_list.pop(0)
    answer = sum + (sum + card_list.pop(0))
    length = len(card_list)

print(answer)

