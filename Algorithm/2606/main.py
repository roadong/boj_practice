import sys

input_line = sys.stdin.readline

N = int(input_line())
M = int(input_line())
node_map = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = []

for _ in range(M):
    u, v = map(int, input_line().split())
    node_map[u].append(v)
    node_map[v].append(u)


def dfs(start_node):
    visited[start_node] = True
    for next_node in node_map[start_node]:
        if not visited[next_node]:
            result.append(next_node)
            dfs(next_node)


dfs(1)
print(len(result))