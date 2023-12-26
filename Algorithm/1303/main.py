import sys

input_line = sys.stdin.readline

N, M = map(int, input_line().split())

fields = [list(input_line().rstrip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

mask = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = [0, 0]


def bfs(x, y, color):
    cnt = 1
    queue = [(x, y)]
    visited[x][y] = True

    while queue:
        u, v = queue.pop()
        for mask_x, mask_y in mask:
            dx, dy = mask_x + u, mask_y + v
            if 0 <= dx < M and 0 <= dy < N:
                if not visited[dx][dy] and fields[dx][dy] == color:
                    visited[dx][dy] = True
                    cnt += 1
                    queue.append((dx, dy))

    return cnt


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if fields[i][j] == "W":
                result[0] += bfs(i, j, "W") ** 2
            else:
                result[1] += bfs(i, j, "B") ** 2

print(*result)
