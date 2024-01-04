import sys
from collections import deque

input_line = sys.stdin.readline

N, M, V = map(int, input_line().split())

tree = [[] for _ in range(N + 1)]
dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

for _ in range(M):
    v1, v2 = map(int, input_line().split())
    tree[v1].append(v2)
    tree[v2].append(v1)
    tree[v1].sort()
    tree[v2].sort()

dfs_result = []


def dfs(v):
    if not dfs_visited[v]:
        dfs_visited[v] = True
    dfs_result.append(v)
    for next_v in tree[v]:
        if not dfs_visited[next_v]:
            dfs(next_v)


bfs_result = []


def bfs(v):
    d_queue = deque([v])
    bfs_visited[v] = True
    while d_queue:
        x = d_queue.popleft()
        bfs_result.append(x)
        for next_v in tree[x]:
            if not bfs_visited[next_v]:
                bfs_visited[next_v] = True
                d_queue.append(next_v)


dfs(V)
bfs(V)
print(*dfs_result)
print(*bfs_result)
