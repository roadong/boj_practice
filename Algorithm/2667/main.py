import sys

input_line = sys.stdin.readline

N = int(input_line())

house_map = [list(map(int, list(input_line().rstrip().split(' ')))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
move_mask = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = []


def dfs(x, y, cnt):
    visited[x][y] = True

    for u, v in move_mask:
        dx, dy = x + u, y + v
        if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy] and house_map[dx][dy] == 1:
            cnt = dfs(dx, dy, cnt + 1)

    return cnt


for i in range(N):
    for j in range(N):
        if not visited[i][j] and house_map[i][j] == 1:
            result.append(dfs(i, j, 1))

print(len(result))
for n in sorted(result):
    print(n)