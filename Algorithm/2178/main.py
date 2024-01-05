import sys
from collections import deque

input_line = sys.stdin.readline
N, M = map(int, input_line().split())
labyrinth_map = [list(map(int, list(input_line().rstrip()))) for _ in range(N)]
visited = [[(False, 0)] * M for _ in range(N)]
move_mask = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y):
    d_queue = deque([(x, y)])
    visited[x][y] = (True, 1)
    cnt = 1
    while d_queue:
        u, v = d_queue.popleft()

        for mask_x, mask_y in move_mask:
            dx, dy = u + mask_x, v + mask_y
            cnt += 1
            if 0 <= dx < N and 0 <= dy < M:
                if not visited[dx][dy][0] and labyrinth_map[dx][dy] == 1:
                    d_queue.append((dx, dy))
                    visited[dx][dy] = (True, min(cnt, visited[u][v][1] + 1))


bfs(0, 0)
print(visited[N-1][M-1][1])
