from collections import deque
from sys import stdin

input_line = stdin.readline


N, M = map(int, input_line().rstrip().split())

campus_map = [list(input_line().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
move_mask = [(1, 0), (-1, 0), (0, 1), (0, -1)]

start = (0, 0)
person_location = []
for i in range(N):
    for j in range(M):
        if campus_map[i][j] == 'I':
            start = (i, j)
            visited[i][j] = True
        elif campus_map[i][j] == 'P':
            person_location.append((i, j))
        else:
            continue


def bfs(node):
    d_queue = deque([node])

    while d_queue:
        x, y = d_queue.popleft()
        for mask_x, mask_y in move_mask:
            dx, dy = x + mask_x, y + mask_y
            if 0 <= dx < N and 0 <= dy < M:
                if not visited[dx][dy] and campus_map[dx][dy] != 'X':
                    visited[dx][dy] = True
                    d_queue.append((dx, dy))


bfs(start)
res = 0
for p_x, p_y in person_location:
    if visited[p_x][p_y]:
        res += 1

print(res if res != 0 else 'TT')
