s = input()
array_s = []

for i in range(len(s)):
    array_s.append(int(s[i]))

result = array_s[0]

for i in range(1, len(array_s)):
    if array_s[i] <= 1 or result <= 1:
        result += array_s[i]
    else:
        result *= array_s[i]

print(result)
