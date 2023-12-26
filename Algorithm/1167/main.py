import sys
from collections import deque

input_line = sys.stdin.readline

V = int(input_line())
edges = [[] for _ in range(V + 1)]

for _ in range(V):
    connect_info = list(input_line().split())

    base_p = int(connect_info[0])
    # 3 5 7 9
    for i in range(len(connect_info) // 2 - 1):
        edge, weight = int(connect_info[2 * i + 1]), int(connect_info[2 * i + 2])
        edges[base_p].append((edge, weight))


def dfs(start_edge):
    # 하나씩 방문
    visited = [False] * (V + 1)
    d_queue = deque()
    visited[start_edge] = True
    d_queue.append(start_edge)
    dfs_result = [0, 0]
    distance = [0] * (V + 1)
    # 모두 탐색할 때까지
    while d_queue:
        next_edge = d_queue.popleft()

        # 엣지와 연결된 모든 간선을 검색
        for v, w in edges[next_edge]:
            # v를 방문하지 않았다면
            if not visited[v]:
                visited[v] = True
                # 다음 탐색을 위해 큐에 넣어준다
                d_queue.append(v)
                # 시작엣지에서 V까지의 거리는 시작엣지에서 next_edge까지의 거리와 nextedge에서 w의 사이의 거리 합
                distance[v] = distance[next_edge] + w
                if distance[v] > dfs_result[1]:
                    dfs_result = v, distance[v]

    return dfs_result


v, w = dfs(1) # 1부터 가장 먼 노드와 거리를 구한다 (가장 먼 노드 정점중 하나를 구함)
print(dfs(v)[1]) # 먼저 구한 정점에서 먼노드를 구한다면 그건 트리지름과 같다


