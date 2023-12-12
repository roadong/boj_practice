import sys
sys.setrecursionlimit(10 ** 5)

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

# LCA algorithm => dfs base
N = int(input())

visited = [False] * (N + 1)
edges = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
depth = [0] * (N + 1)


for _ in range(N - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)


# 깊이 탐색 (그래프 깊이 구하기)
def dfs(x, depth_idx):
    visited[x] = True
    depth[x] = depth_idx

    node: int
    for node in edges[x]:
        if visited[node]:
            continue
        parent[node] = x
        dfs(node, depth_idx + 1)


def lca(v1, v2):
    # 깊이 맞추기 (같은 깊이가 되어야 최소 조상을 찾을 수 있다)
    while depth[v1] != depth[v2]:
        # 깊이가 높은 쪽의 부모를 가져온다
        if depth[v1] > depth[v2]:
            v1 = parent[v1]
        else:
            v2 = parent[v2]

    # 깊이가 같으면 서로 같은 부모를 가리킬 때까지 부모를 가져온다
    while v1 != v2:
        v1 = parent[v1]
        v2 = parent[v2]

    return v1


# 노드 탐색
dfs(1, 0)
M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
