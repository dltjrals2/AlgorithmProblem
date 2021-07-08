s = input()
array_string = []
array_sum = 0
result = ""

for i in range(len(s)):
    if ord(s[i]) >= 65:
        array_string.append(s[i])
    else:
        array_sum += int(s[i])

array_string.sort()
for i in range(len(array_string)):
    result += array_string[i]

result += str(array_sum)

print(result)
