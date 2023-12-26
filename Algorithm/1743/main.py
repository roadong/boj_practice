import sys
from collections import deque

input_line = sys.stdin.readline

# N: 세로, M:가로, K: 갯수
N, M, K = map(int, input_line().split())

space = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
q_find = []

for _ in range(K):
    r, c = map(int, input_line().split())
    space[r-1][c-1] = 1
    q_find.append((r-1, c-1))

mask = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0

while q_find:
    x, y = q_find.pop()
    if visited[x][y]:
        continue

    visited[x][y] = True
    cnt = 1
    connect_waste = [(x, y)]
    while connect_waste:
        x, y = connect_waste.pop()
        for i, j in mask:
            dx, dy = x + i, y + j
            if 0 <= dx < N and 0 <= dy < M:
                if not visited[dx][dy] and space[dx][dy] == 1:
                    visited[dx][dy] = True
                    cnt += 1
                    connect_waste.append((dx, dy))

    result = max(result, cnt)

print(result)
