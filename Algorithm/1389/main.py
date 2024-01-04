import sys
from collections import deque

input_line = sys.stdin.readline

N, M = map(int, input_line().split())

relation_tree = [[] for _ in range(N + 1)]
memoization = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input_line().split())
    relation_tree[a].append(b)
    relation_tree[b].append(a)
    memoization[a][b] = 1
    memoization[b][a] = 1
    memoization[a][a] = 0
    memoization[b][b] = 0


def bfs(v):
    visited = [False] * (N + 1)
    d_queue = deque([v])
    visited[v] = True

    while d_queue:
        next_v = d_queue.popleft()
        for i in relation_tree[next_v]:
            if not visited[i]:
                visited[i] = True
                d_queue.append(i)
                if memoization[v][i] != 1:
                    memoization[v][i] = min(memoization[v][i], memoization[v][next_v] + 1)


for i in range(1, N + 1):
    bfs(i)

result = [0, sys.maxsize]
for i in range(1, N + 1):
    kevin_bacon_num = sum(memoization[i][1:])
    if kevin_bacon_num < result[1]:
        result[0] = i
        result[1] = kevin_bacon_num


print(result[0])
