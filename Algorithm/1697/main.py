import sys
from collections import deque

input_line = sys.stdin.readline

N, K = map(int, input_line().split())

visited = [(False, sys.maxsize)] * 100001


def bfs(n):
    d_queue = deque([n])
    visited[n] = (True, 0)

    cnt = 0
    while d_queue:
        x = d_queue.popleft()

        cnt += 1
        if 0 <= x - 1 and not visited[x - 1][0]:
            visited[x - 1] = (True, min(cnt, visited[x][1] + 1))
            d_queue.append(x - 1)

        if x + 1 <= 100000 and not visited[x + 1][0]:
            visited[x + 1] = (True, min(cnt, visited[x][1] + 1))
            d_queue.append(x + 1)

        if 2 * x <= 100000 and not visited[2 * x][0]:
            visited[2 * x] = (True, min(cnt, visited[x][1] + 1))
            d_queue.append(2 * x)


bfs(N)
print(visited[K][1])
