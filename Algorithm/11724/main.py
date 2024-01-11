import sys
from collections import deque

input_line = sys.stdin.readline

N, M = map(int, input_line().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input_line().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    d_queue = deque([start])
    # 시작 노드에서 모든 연결을 탐색하기 때문에 방문 체크
    visited[start] = True

    while d_queue:
        x = d_queue.popleft()
        for end in graph[x]:
            if not visited[end]:
                visited[end] = True
                d_queue.append(end)

res = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        res += 1

print(res)

