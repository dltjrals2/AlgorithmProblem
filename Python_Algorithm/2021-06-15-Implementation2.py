n = int(input()) # N 입력 받기
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i):
                count += 1
            elif '3' in str(j):
                count += 1
            elif '3' in str(k):
                count += 1

print(count)
