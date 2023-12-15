import sys

input_line = sys.stdin.readline

R, C = map(int, input_line().split())
visited = [[False] * C for _ in range(R)]

pipelines = [list(input_line().rstrip()) for _ in range(R)]


def dfs(x, y):
    if y == C - 1:
        return True

    for mask_x in [-1, 0, 1]:
        n_x = x + mask_x
        n_y = y + 1

        # 범위 내
        if 0 <= n_x < R and 0 <= n_y < C:
            # 미방문 & 장애물 아님
            if not visited[n_x][n_y] and pipelines[n_x][n_y] != "x":
                visited[n_x][n_y] = True
                if dfs(n_x, n_y):
                    return True

    return False


sol_cnt = 0
for i in range(R):
    if dfs(i, 0):
        sol_cnt += 1

print(sol_cnt)
