n = input()
len_n = len(n)
left_sum = 0
right_sum = 0

for i in range(0, int(len_n / 2)):
    left_sum += int(n[i])

for j in range(int(len_n / 2), int(len_n)):
    right_sum += int(n[j])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
