from sys import stdin

input_line = stdin.readline

# 15 15
# 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1

N, M = map(int, input_line().split())

path_map = [list(map(int, input_line().rstrip().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
move_masks = [(1, 0), (-1, 0), (0, 1), (0, -1)]
start_node = []
for i in range(N):
    for j in range(M):
        if path_map[i][j] == 2:
            start_node.append(i)
            start_node.append(j)
        elif path_map[i][j] == 0:
            visited[i][j] = 0


def bfs(x, y):
    from collections import deque
    d_queue = deque([(x, y)])
    visited[x][y] += 1

    while d_queue:
        u, v = d_queue.popleft()

        for mask_x, mask_y in move_masks:
            dx, dy = u + mask_x, v + mask_y
            if 0 <= dx < N and 0 <= dy < M and (visited[dx][dy] == -1):
                visited[dx][dy] = visited[u][v] + 1
                d_queue.append((dx, dy))


bfs(start_node[0], start_node[1])

for arr in visited:
    print(*arr)
