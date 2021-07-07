s = input()
array_s = []
zero_count = 0
one_count = 0

for i in range(len(s)):
    array_s.append(int(s[i]))

if array_s[0] == 1:
    zero_count += 1
else:
    one_count += 1

for i in range(len(array_s) - 1):
    if array_s[i] != array_s[i + 1]:
        if array_s[i + 1] == 1:
            zero_count += 1
        else:
            one_count += 1

print(min(zero_count, one_count))
