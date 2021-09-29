from collections import deque

# n, k : 크기, 바이러스 종류
n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

# 오름차순 정렬
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 상, 하, 좌, 우
dx = [0 ,0, -1, 1]
dy = [1, -1, 0, 0]

while q:
    virus_kind, time, x, y = q.popleft()
    if time == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx >= 0 and ny < n and ny >= 0:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus_kind
                q.append((virus_kind, time + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
