import sys
from collections import deque

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N = int(input())
arr = []
maxN = 0

near_node = [[0, 0, 1, -1], [1, -1, 0, 0]]

for x in range(N):
    arr.append(list(map(int, input().split())))
    for y in range(N):
        if arr[x][y] > maxN:
            maxN = arr[x][y]


def bfs(a, b, val, visited):
    deq = deque()
    deq.append((a, b))
    visited[a][b] = True

    while deq:
        x, y = deq.popleft()

        for near in range(4):
            nx = x + near_node[0][near]
            ny = y + near_node[1][near]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > val and not visited[nx][ny]:
                    visited[nx][ny] = True
                    deq.append((nx, ny))


result = 0
for i in range(maxN):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for a in range(N):
        for b in range(N):
            if arr[a][b] > i and not visited[a][b]:
                bfs(a, b, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt


print(result)
