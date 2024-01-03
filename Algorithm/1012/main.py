import sys

input_line = sys.stdin.readline

T = int(input_line())
mask = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(i, j):
    queue = [(i, j)]
    visited[i][j] = True

    while queue:
        x, y = queue.pop()
        for u, v in mask:
            dx, dy = x + u, y + v
            if 0 <= dx < M and 0 <= dy < N:
                if not visited[dx][dy] and farm_field[dx][dy] == 1:
                    visited[dx][dy] = True
                    queue.append((dx, dy))


for _ in range(T):
    # M 가로 N 세로 K 갯수
    M, N, K = map(int, input_line().split())

    farm_field = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input_line().split())
        farm_field[x][y] = 1

    result = 0
    d_queue = []
    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                if farm_field[i][j] == 1:
                    result += 1
                    bfs(i, j)
                else:
                    visited[i][j] = True

    print(result)




