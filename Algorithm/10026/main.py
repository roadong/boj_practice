import sys
from collections import deque

input_line = sys.stdin.readline

N = int(input_line())

rgb = [list(input_line().rstrip()) for _ in range(N)]
move_mask = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = [0, 0]


# 2번 탐색 (normal, rg group)
def dfs(x, y, colors, visited):
    d_queue = deque([(x, y)])
    visited[x][y] = True

    while d_queue:
        u, v = d_queue.popleft()
        for mask_x, mask_y in move_mask:
            dx, dy = u + mask_x, v + mask_y
            if 0 <= dx < N and 0 <= dy < N:
                if not visited[dx][dy] and rgb[dx][dy] in colors:
                    visited[dx][dy] = True
                    dfs(dx, dy, colors, visited)


def calc_normal_view():
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if rgb[i][j] == 'B':
                    dfs(i, j, ['B'], visited)
                    result[0] += 1
                elif rgb[i][j] == 'G':
                    dfs(i, j, ['G'], visited)
                    result[0] += 1
                else:
                    dfs(i, j, ['R'], visited)
                    result[0] += 1


def calc_abnormal_view():
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if rgb[i][j] == 'B':
                    dfs(i, j, ['B'], visited)
                    result[1] += 1
                else:
                    dfs(i, j, ['R', 'G'], visited)
                    result[1] += 1


calc_normal_view()
calc_abnormal_view()
print(*result)
