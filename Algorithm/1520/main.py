import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

M, N = map(int, input().split())
visited = [[-1] * N for _ in range(M)]
arr = [list(map(int, input().split())) for _ in range(M)]
move_mask = [[0, 1, 0, -1], [1, 0, -1, 0]]


def find_route(x, y):
    # find!
    if x == M - 1 and y == N - 1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        next_x = x + move_mask[0][i]
        next_y = y + move_mask[1][i]

        if 0 <= next_x < M and 0 <= next_y < N:
            if arr[x][y] > arr[next_x][next_y]:
                visited[x][y] += find_route(next_x, next_y)

    return visited[x][y]


print(find_route(0, 0))
